from . import api
from .resource import SecureCustomerResource
from .. import db
from ..models import CartItem, Item
from flask_restplus import reqparse

cart_post_parser = reqparse.RequestParser()
cart_post_parser.add_argument('item_id', type=int, required=True)

cart_put_parser = reqparse.RequestParser()
cart_put_parser.add_argument('item_id', type=int, required=True)
cart_put_parser.add_argument('selected', type=bool, required=True)
cart_put_parser.add_argument('count', type=int, required=True)

cart_del_parser = reqparse.RequestParser()
cart_del_parser.add_argument('item_id', type=int, required=True)


@api.route('/cart')
class Cart(SecureCustomerResource):
    """
    URL : /api/cart
    args: (1) customer_id 用户id
    extra : 需要用户登录凭证
    """
    def post(self, auth_customer):
        """
        POST: 添加商品到购物车
        args :  (1) item_id, 商品id
        return: (1) 成功, status code 201
                (2) 失败, status code 400
                    a. message, str, 错误信息
                (3) 权限不足，status code 401
        """
        args = cart_post_parser.parse_args()

        if not Item.query.get(args.item_id):
            return {'message': 'Invalid item id'}, 400

        new_cart = CartItem(customer_id=auth_customer.id,
                            item_id=args.item_id,
                            selected=True,
                            count=1)

        # 如果该商品已经存在，返回400错误
        try:
            db.session.add(new_cart)
            db.session.commit()
        except:
            return {'message': 'Item already exist in cart!'}, 400

        return {}, 201

    def get(self, auth_customer):
        """
        GET: 获取购物车商品信息
        args : 无
        return: (1) 成功, status code 200
                    a. items, {item_id, count, selected}, 购物车信息
                (2) 失败, status code 400
                    a. message, str, 错误信息
                (3) 权限不足，status code 401
        """
        items = CartItem.query.filter_by(customer_id=auth_customer.id).all()
        output = []
        for item in items:
            item_data = {}
            item_data['item_id'] = item.item_id
            item_data['selected'] = item.selected
            item_data['count'] = item.count
            output.append(item_data)
        return {'items': output}, 200

    def put(self, auth_customer):
        """
        PUT: 更新购物车某一条商品记录
        args:   (1) item_id, 商品id
                (2) selected, bool, 是否选中
                (3) count, int, 个数
        return: (1) 成功，status code 200
                (2) 失败，status code 400
                    a. message, str, 错误信息
                (3) 权限不足，status code 401
        """
        args = cart_put_parser.parse_args()
        item = CartItem.query.filter_by(customer_id=auth_customer.id,
                                        item_id=args.item_id).first_or_404()

        item.selected = args.selected
        item.count = args.count

        db.session.commit()
        return {}, 200

    def delete(self, auth_customer):
        """
        DELETE: 删除购物车某一条商品记录
        args:   (1) item_id, 商品id
        return: (1) 成功, status code 200
                (2) 失败, status code 400
                    a. message, str, 错误信息
                (3) 权限不足，status code 401
        """
        args = cart_del_parser.parse_args()
        item = CartItem.query.filter_by(customer_id=auth_customer.id,
                                        item_id=args.item_id).first_or_404()

        db.session.delete(item)
        db.session.commit()
        return {}, 200
