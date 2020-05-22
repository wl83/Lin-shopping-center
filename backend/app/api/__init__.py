""" API Blueprint Application """

from flask import Blueprint
from flask_restplus import Api

api_bp = Blueprint('api_bp', __name__, url_prefix='/api')
api = Api(api_bp)


# @api_bp.after_request
# def add_header(response):
#     response.headers['Access-Control-Allow-Origin'] = '*'
#     response.headers['Access-Control-Allow-Methods'] = 'GET,POST'
#     response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
#     return response


# 导入相应 API
from .customer import *  # NOQA
from .captcha import *   # NOQA
from .address import *   # NOQA
from .review import *    # NOQA
from .cart import *      # NOQA
from .order import *     # NOQA
from .item import *      # NOQA
from .shop import *      # NOQA
