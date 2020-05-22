from . import api
from .resource import SecureCustomerResource
from .. import db
from ..models import Address
from flask_restplus import reqparse, Resource

address_post_parser = reqparse.RequestParser()
address_post_parser.add_argument('receiver', required=True)
address_post_parser.add_argument('phone', required=True)
address_post_parser.add_argument('address', required=True)

address_put_parser = reqparse.RequestParser()
address_put_parser.add_argument('address_id', required=True, type=int, help='Invalid address ID')
address_put_parser.add_argument('receiver')
address_put_parser.add_argument('phone')
address_put_parser.add_argument('address')

address_del_parser = reqparse.RequestParser()
address_del_parser.add_argument('address_id', required=True, type=int, help='Invalid address ID')


@api.route('/address')
class AddressApi(SecureCustomerResource):
    """
    args:
        (1) customer_id 用户id
    extra : 需要用户登录凭证
    """
    def post(self, auth_customer):
        """
        (1) POST：保存用户新建的地址
        args:(1) receiver, str, 用户姓名;
             (2) phone, str, 手机号码;
             (3) address, str, 收货地址;
        return: (1) 成功，status code 200
                (2) 失败，status code 400
                        a. message, str, 错误信息
                (3) 权限不足，status code 401
        """
        args = address_post_parser.parse_args()
        new_address = Address(receiver=args['receiver'],
                              customer_id=auth_customer.id,
                              phone=args['phone'],
                              address=args['address'])
        db.session.add(new_address)
        db.session.commit()
        return {}, 200

    def get(self, auth_customer):
        """
        (2) GET：获取用户保存的所有地址
        args: 无
        return: (1) 成功，status code 200
                        a. addrs, addr, 地址信息集合
                (2) 失败，status code 400
                        a. message, str, 错误信息
                (3) 权限不足，status code 401
        """
        addresses = Address.query.filter_by(customer_id=auth_customer.id, deleted=False).all()
        output = []
        for address in addresses:
            address_data = {}
            address_data['id'] = address.id
            address_data['receiver'] = address.receiver
            address_data['phone'] = address.phone
            address_data['address'] = address.address
            output.append(address_data)
        return {'addrs': output}, 200

    def put(self, auth_customer):
        """
        (3) PUT：更新某个地址
        args: (1) address_id, int, 地址id;
              (2) receiver（可选）, str, 用户姓名;
              (3) phone（可选）, str, 手机号码;
              (4) address（可选）, str, 收货地址;
        return: (1) 成功，status code 200
                (2) 失败，status code 400
                    a. message, str, 错误信息
                (3) 权限不足，status code 401
        """
        args = address_put_parser.parse_args()
        address = Address.query.get_or_404(args.address_id)

        if args['receiver']:
            address.receiver = args['receiver']
        if args['phone']:
            address.phone = args['phone']
        if args['address']:
            address.address = args['address']
        db.session.commit()
        return {}, 200

    def delete(self, auth_customer):
        """
        (4) DELETE：删除某个地址
        args: (1) address_id, int, 地址id;
        return: (1) 成功，status code 200
                (2) 失败，status code 400
                    a. message, str, 错误信息
                (3) 权限不足，status code 401
        """
        args = address_del_parser.parse_args()
        address = Address.query.get_or_404(args.address_id)
        address.deleted = True
        db.session.commit()

        try:
            db.session.delete(address)
            db.session.commit()
        except:
            return {'message': 'Address was used in some order, archived now'}, 200

        return {}, 200


@api.route('/address/<int:address_id>')
class AddressQuery(Resource):
    """
    根据ID获得地址
    URL : /api/address
    method : GET
    args:   (1) address_id, int, 地址id;
    return: (1) 成功，status code 200
            (2) 失败，status code 400
                a. message, str, 错误信息
    """
    def get(self, address_id):
        address = Address.query.get_or_404(address_id)

        address_data = {}
        address_data['receiver'] = address.receiver
        address_data['phone'] = address.phone
        address_data['address'] = address.address
        address_data['customer_id'] = address.customer_id

        return address_data, 200
