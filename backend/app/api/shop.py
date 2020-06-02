from . import api
from .captcha import check_captcha
from .. import app, db
from ..models import Shop, Item, Review, Order, ItemImage, OrderItem, CartItem
from flask_restplus import Resource, reqparse
from flask import request
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import jwt
import datetime


def require_auth(f):
    """登录请求装饰器"""
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            token = request.headers['Authorization']
            data = jwt.decode(token, app.config['SECRET_KEY'])
            auth_shop = Shop.query.filter_by(id=data['shop_id']).first()
            if not auth_shop:
                raise Exception('Wrong customer id')
        except:
            return {
                'message': 'This request needs correct access token!'
            }, 401, {
                'WWW-Authenticate': 'Basic realm : "Login required!"'
            }
        kwargs['auth_shop'] = auth_shop
        return f(*args, **kwargs)

    return decorated


shop_login_parser = reqparse.RequestParser()
shop_login_parser.add_argument('phone', required=True)
shop_login_parser.add_argument('password', required=True)


@api.route('/shop/login')
class ShopLogin(Resource):
    """
    店铺登陆
    URL : /api/shop/login
    method : GET
    args:   (1) phone , str, 用户手机号;
            (2) password, str, 密码;
    return: (1) 成功，status code 200
                a. token, str, 验证用token
            (2) 信息错误，status code 401
                a. message, str, 错误信息
    """
    def get(self):
        auth = shop_login_parser.parse_args()
        if not auth.phone or not auth.password:
            return {'message': 'Bad login request!'}, 400

        user = Shop.query.filter_by(phone=auth.phone).first()
        if user:
            if check_password_hash(user.password_hash, auth.password):
                token = jwt.encode(
                    {
                        'shop_id': user.id,
                        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60)
                    }, app.config['SECRET_KEY'])
                token = token.decode('UTF-8')
                return {'token': token}, 200

        return {'message': 'Wrong phone or password!'}, 401


shop_reg_parser = reqparse.RequestParser()
shop_reg_parser.add_argument('name', required=True)
shop_reg_parser.add_argument('address', required=True)
shop_reg_parser.add_argument('info', required=True)
shop_reg_parser.add_argument('phone', required=True)
shop_reg_parser.add_argument('password', required=True)
shop_reg_parser.add_argument('captcha_identifer', required=True)
shop_reg_parser.add_argument('captcha_code', required=True)


@api.route('/shop/create')
class ShopRegister(Resource):
    def post(self):
        """
        创建新店铺
        URL : /api/shop/create
        method: POST
        args :  (1) name, str, 店铺名称;
                (2) address, str, 店铺地址;
                (3) info, str, 店铺介绍;
                (4) phone, str, 店铺联系电话;
                (5) password, str, 店铺登录密码
                (6) captcha_identifer, str, 验证码标识;
                (7) captcha_code, str, 用户输入的验证码;
        return: (1) 成功, status code 201
                (2) 失败, status code 400
                    a. message, str, 错误信息
        """
        args = shop_reg_parser.parse_args()

        # 检查验证码
        # if not check_captcha(args.captcha_identifer, args.captcha_code):
        #     return {'message': 'Wrong captcha code!'}, 400

        password_hash = generate_password_hash(args['password'])
        new_shop = Shop(name=args.name,
                        address=args.address,
                        info=args.info,
                        phone=args.phone,
                        password_hash=password_hash)

        # 如果店铺已经存在，返回400错误
        try:
            db.session.add(new_shop)
            db.session.commit()
        except:
            return {'message': 'Phone already exist! Please login.'}, 400

        return {}, 201


@api.route('/shops/<int:shop_id>')
class ShopQuery(Resource):
    def get(self, shop_id):
        """
        GET : 获取店铺信息
        URL : /api/shops/:shop_id
        method: GET
        args:   (1) shop_id, int, 店铺id;
        return: (1) 成功, status code 200
                    a. name, str, 店铺名称;
                    b. address, str, 店铺地址;
                    c. info, str, 店铺介绍;
                    d. phone, str, 店铺联系电话;
                    e. created_time, str, 店铺创建时间;
                (2) 失败, status code 400
                    a. message, str, 错误信息;
        """
        shop = Shop.query.get_or_404(shop_id)

        shop_data = {}
        shop_data['name'] = shop.name
        shop_data['address'] = shop.address
        shop_data['info'] = shop.info
        shop_data['phone'] = shop.phone
        shop_data['created_time'] = str(shop.created_time)
        return shop_data, 200


shop_put_parser = reqparse.RequestParser()
shop_put_parser.add_argument('name')
shop_put_parser.add_argument('address')
shop_put_parser.add_argument('info')
shop_put_parser.add_argument('phone')


@api.route('/shop')
class ShopManagement(Resource):
    method_decorators = [require_auth]

    def get(self, auth_shop):
        shop_data = {}
        shop_data['shop_id'] = auth_shop.id
        shop_data['phone'] = auth_shop.phone
        shop_data['name'] = auth_shop.name
        shop_data['address'] = auth_shop.address
        shop_data['info'] = auth_shop.info

        return shop_data, 200

    def put(self, auth_shop):
        """
        PUT : 更新店铺信息
        URL : /api/shops/:shop_id
        extra : 需要店铺登录凭证
        method: PUT
        args :  (1) shop_id, int, 店铺id;
                (2) name(可选), str, 店铺名称;
                (3) address(可选), str, 店铺地址;
                (4) info(可选), str, 店铺介绍;
                (5) phone(可选), str, 店铺联系电话;
        return: (1) 成功, status code 200
                (2) 失败, status code 400
                    a. message, str, 错误信息
                (3) 权限不足，status code 401
        """
        args = shop_put_parser.parse_args()
        auth_shop.name = args['name'] or auth_shop.name
        auth_shop.address = args['address'] or auth_shop.address
        auth_shop.info = args['info'] or auth_shop.info
        auth_shop.phone = args['phone'] or auth_shop.phone

        db.session.commit()
        return {}, 200

    def delete(self, auth_shop):
        """
        注销店铺
        URL : /api/shop
        extra : 需要店铺登录凭证
        method: DELETE
        args:   (1) shop_id, int, 店铺id;
        return: (1) 成功, status code 200
                (2) 失败, status code 400
                    a. message, str, 错误信息
                (3) 权限不足，status code 401
        """
        # 注销店铺时：1.先删除与该商品有关的评论
        #           2.再删除与该商品有关的order_item
        #           3.再删除与该商品有关的order
        #           4.再删除与该商品有关的images
        #           5.再删除购物车中的商品
        items = Item.query.filter_by(shop_id=auth_shop.id).all()
        for item in items:
            # 1.先删除与该商品有关的评论
            reviews = Review.query.filter_by(item_id=item.id).all()
            for review in reviews:
                db.session.delete(review)
            # 2.再删除与该商品有关的order_item
            # 3.再删除与该商品有关的order
            order_items = OrderItem.query.filter_by(item_id=item.id).all()
            orders = []
            for order_item in order_items:
                order = Order.query.filter_by(id=order_item.order_id).first_or_404()
                orders.append(order)
                db.session.delete(order_item)
            for order in orders:
                db.session.delete(order)
            # 4.再删除与该商品有关的images
            images = ItemImage.query.filter_by(item_id=item.id).all()
            for image in images:
                db.session.delete(image)
            # 5.再删除购物车中的商品
            cart_items = CartItem.query.filter_by(item_id=item.id).all()
            for cart_item in cart_items:
                db.session.delete(cart_item)

        for item in items:
            db.session.delete(item)
            db.session.commit()

        db.session.delete(auth_shop)
        db.session.commit()
        return {}, 200
