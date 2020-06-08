from . import api
from .resource import SecureCustomerResource, SecureShopResource
from .. import db
from ..models import Order, Item, OrderItem, CartItem, Status, Review, Address
from flask_restplus import reqparse
from sqlalchemy import select
import datetime

# the number of each group of orders
GROUP_COUNT = 5

order_post_parser = reqparse.RequestParser()
order_post_parser.add_argument('address_id', type=int, required=True)

order_get_parser = reqparse.RequestParser()
order_get_parser.add_argument('group_index', type=int)

order_put_parser = reqparse.RequestParser()
order_put_parser.add_argument('status', type=int, required=True)


@api.route('/order/create')
class OrderCreate(SecureCustomerResource):
    """
    用户下单
    URL : /api/order/create
    method : POST
    extra : 需要用户登录凭证
    args :  (1) address_id, int, 地址id
    return: (1) 成功, status code 201
                a. order_id, int, 订单id
            (2) 失败, status code 400
                a. message, str, 错误信息
            (3) 权限不足，status code 401
    """
    def post(self, auth_customer):
        args = order_post_parser.parse_args()

        if not Address.query.get(args.address_id):
            return {'message': 'Invalid address id'}, 400

        new_order = Order(status=Status.pending,
                          customer_id=auth_customer.id,
                          address_id=args.address_id,
                          payment_amount=0)
        db.session.add(new_order)
        db.session.commit()

        cart_items = CartItem.query.filter_by(customer_id=auth_customer.id, selected=True).all()
        payment_amount = 0    # 订单总额
        for cart_item in cart_items:
            item = Item.query.filter_by(id=cart_item.item_id).first()
            if not item or cart_item.count > item.in_stock:
                db.session.rollback()
                db.session.delete(new_order)
                db.session.commit()
                return {
                    'message': 'Item ' + str(cart_item.item_id) + ' not available',
                    'item_id': cart_item.item_id
                }, 400

            new_order_item = OrderItem(order_id=new_order.id,
                                       item_id=cart_item.item_id,
                                       amount=cart_item.count,
                                       price_paid=item.current_price)

            # 更新销量
            item.in_stock = item.in_stock - cart_item.count
            item.sales = item.sales + cart_item.count

            # 删除购物车中的商品
            db.session.delete(cart_item)
            db.session.add(new_order_item)
            # 计算订单总额
            payment_amount += cart_item.count * item.current_price

        new_order.payment_amount = payment_amount
        db.session.commit()
        return {'order_id': new_order.id}, 201


@api.route('/customer/orders')
class OrderHisQuery(SecureCustomerResource):
    """
    用户历史订单查询(时间倒序排序)
    URL : /api/customer/orders
    method : GET
    extra : 需要用户登录凭证
    args :  (1) group_index, int, 组号, 默认为0
    return: (1) 成功, status code 200
                a. order_ids, {int}, 用户第index组订单的id集合
            (2) 失败, status code 400
                a. message, str, 错误信息
            (3) 权限不足，status code 401
    """
    def get(self, auth_customer):
        args = order_get_parser.parse_args()
        group = args.group_index or 0

        orders = Order.query.filter_by(customer_id=auth_customer.id).order_by(Order.id.desc())

        total = orders.count()

        ordersPage = orders.paginate(page=1 + group, per_page=GROUP_COUNT)
        output = []
        for order in ordersPage.items:
            output.append(order.id)

        return {'orders': output, 'total': total}, 200


@api.route('/shop/orders')
class OrderShopQuery(SecureShopResource):
    """
    商家历史订单查询(时间倒序排序)
    URL : /api/shop/orders
    method : GET
    extra : 需要商家登录凭证
    args :  (1) group_index, int, 组号, 默认为0
    return: (1) 成功, status code 200
                a. order_ids, {int}, 用户第index组订单的id集合
            (2) 失败, status code 400
                a. message, str, 错误信息
            (3) 权限不足，status code 401
    """
    def get(self, auth_shop):
        shop_items = Item.query.filter_by(shop_id=auth_shop.id).all()
        order_ids = []
        order_datas = []
        for shop_item in shop_items:
            order_items = OrderItem.query.filter_by(item_id=shop_item.id).all()
            for order_item in order_items:
                if order_item.order_id not in order_ids:
                    order_ids.append(order_item.order_id)
                    order_data = {}
                    order_data['items'] = []
                    order_data['items'].append({ 'item_id': order_item.item_id, 'amount': order_item.amount })
                    order_data['order_id'] = order_item.order_id
                    order_data['price'] = str(round(order_item.amount * order_item.price_paid, 2))
                    order_datas.append(order_data)
                else:
                    index = order_ids.index(order_item.order_id)
                    order_datas[index]['price'] = str(round(float(order_datas[index]['price']) + float(order_item.amount * order_item.price_paid), 2))
                    order_datas[index]['items'].append({ 'item_id': order_item.item_id, 'amount': order_item.amount })

        return {'orders': order_datas}, 200


@api.route('/shop/orders/<int:order_id>')
class OrderQueryShop(SecureShopResource):
    """
    GET: 获取订单信息
    URL : /api/shop/orders/:order_id
    extra : 需要商户登录凭证
    args :  (1) order_id, int, 订单id
    return: (1) 成功, status code 200
                a. customer_id, int, 用户id
                b. address, {receiver, phone, address}, 地址
                c. status, enum, 订单状态枚举值
                d. created_time, datetime, 订单创建时间
                e. payment_time, datetime, 订单付款时间
                f. payment_amount, int, 订单总价（用户才有）
                g. items, {item_id, count, review_id}, 订单商品列表（商户只能看到商户的商品）
            (2) 失败, status code 400
                a. message, str, 错误信息
            (3) 权限不足，status code 401
    """
    def get(self, order_id, auth_shop):
        order = Order.query.filter_by(id=order_id).first_or_404()
        order_items = order.items
        order_data = {}
        order_data['customer_id'] = order.customer_id

        if order.address_id:
            address = Address.query.get(order.address_id)
            address_data = {}
            address_data['receiver'] = address.receiver
            address_data['phone'] = address.phone
            address_data['address'] = address.address
            order_data['address'] = address_data

        order_data['status'] = order.status.value
        order_data['created_time'] = str(order.created_time)
        order_data['payment_time'] = str(order.payment_time)
        order_data['payment_amount'] = str(round(order.payment_amount, 2))

        output = []
        for order_item in order_items:
            item = Item.query.filter_by(id=order_item.item_id, shop_id=auth_shop.id).first()
            if not item:
                continue

            review = Review.query.filter_by(item_id=order_item.item_id).first()

            item_data = {}
            item_data['item_id'] = item.id
            item_data['count'] = order_item.amount
            if review:
                item_data['review_id'] = review.id
            output.append(item_data)

        if len(output) == 0:
            return {'message': 'No item in this order belongs to this shop.'}, 401

        order_data['items'] = output
        return order_data, 200

    def put(self, order_id, auth_shop):
        """
        PUT: 更新订单信息
        URL : /api/customer/orders/:order_id 或 /api/shop/orders/:order_id
        extra : 需要用户登录凭证或商户登录凭证
        args:   (1) order_id, int, 订单id
                (2) status, int, 状态枚举值
                    return:(1) 成功，status code 200
                (2) 失败，status code 400
                    a. message, str, 错误信息
                (3) 权限不足，status code 401
        """
        args = order_put_parser.parse_args()
        order = Order.query.filter_by(id=order_id).first_or_404()
        order_items = order.items

        for order_item in order_items:
            item = Item.query.filter_by(id=order_item.item_id, shop_id=auth_shop.id).first()
            if item:
                order.status = Status(args.status)
                db.session.commit()
                return {}, 200

        return {'message': 'No item in this order belongs to this shop.'}, 401


@api.route('/customer/orders/<int:order_id>')
class OrderQueryCustomer(SecureCustomerResource):
    """
    GET: 获取订单信息
    URL : /api/customer/orders/:order_id
    extra : 需要用户登录凭证
    args :  (1) order_id, int, 订单id
    return: (1) 成功, status code 200
                a. customer_id, int, 用户id
                b. status, enum, 订单状态枚举值
                c. created_time, datetime, 订单创建时间
                d. payment_time, datetime, 订单付款时间
                e. payment_amount, int, 订单总价
                f. items, {item_id, count, review_id}, 订单商品列表
            (2) 失败, status code 400
                a. message, str, 错误信息
            (3) 权限不足，status code 401
    """
    def get(self, order_id, auth_customer):
        order = Order.query.filter_by(id=order_id).first_or_404()
        order_items = order.items
        order_data = {}
        order_data['customer_id'] = order.customer_id
        order_data['address_id'] = order.address_id
        order_data['status'] = order.status.value
        order_data['created_time'] = str(order.created_time)
        order_data['payment_time'] = str(order.payment_time)
        order_data['payment_amount'] = str(round(order.payment_amount, 2))

        output = []
        for order_item in order_items:
            item = Item.query.filter_by(id=order_item.item_id).first()
            review = Review.query.filter_by(item_id=order_item.item_id).first()

            item_data = {}
            item_data['item_id'] = item.id
            item_data['count'] = order_item.amount
            if review:
                item_data['review_id'] = review.id
            output.append(item_data)

        order_data['items'] = output
        return order_data, 200

    def put(self, order_id, auth_customer):
        """
        PUT: 更新订单信息
        URL : /api/customer/orders/:order_id 或 /api/shop/orders/:order_id
        extra : 需要用户登录凭证或商户登录凭证
        args:   (1) order_id, int, 订单id
                (2) status, int, 状态枚举值
        return: (1) 成功，status code 200
                (2) 失败，status code 400
                    a. message, str, 错误信息
                (3) 权限不足，status code 401
        """
        args = order_put_parser.parse_args()
        order = Order.query.filter_by(id=order_id).first_or_404()
        order.status = Status(args.status)
        db.session.commit()
        return {}, 200

@api.route('/shop/report')
class OrderReport(SecureShopResource):
    def get(self, auth_shop):
        """
        GET: 获取报表信息
        URL : /api/shop/report
        extra : 需要商户登录凭证
        args:  无
        return: (1) 成功，status code 200
                    paymentList
                (2) 失败，status code 400
                    a. message, str, 错误信息
                (3) 权限不足，status code 401
        """
        output = []
        now_time = datetime.date.today()
        one_day = datetime.timedelta(days=1)

        time = now_time + one_day
        for i in range(7):
            time = time - one_day
            payment_amount = 0
            items = Item.query.filter_by(shop_id=auth_shop.id)
            for item in items:
                itemQuery = Item.query.filter_by(id=item.id).first_or_404()
                order_items = OrderItem.query.filter_by(item_id=item.id)
                for order_item in order_items:
                    orderQuery = Order.query.filter_by(id=order_item.order_id).first_or_404()
                    if orderQuery.created_time == time:
                        payment_amount += order_item.amount * itemQuery.current_price
            output.append(str(round(payment_amount, 2)))

        return {'paymentList': output}
