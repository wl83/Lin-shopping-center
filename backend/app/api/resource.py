from .customer import require_auth as customer_auth
from .shop import require_auth as shop_auth
from flask_restplus import Resource


class SecureCustomerResource(Resource):
    """ Calls require_auth decorator on all requests """
    method_decorators = [customer_auth]


class SecureShopResource(Resource):
    """ Calls require_auth decorator on all requests """
    method_decorators = [shop_auth]
