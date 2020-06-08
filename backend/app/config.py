"""
FLASK 全局配置

部署时，环境变量从 .flaskenv 文件中载入
"""

import os
from app import app


class Config(object):
    FLASK_ENV = os.getenv('FLASK_ENV', 'development')
    FLASK_APP = os.getenv('FLASK_APP', 'app')

    SECRET_KEY = os.getenv('SECRET_KEY', 'secret')

    APP_DIR = os.path.dirname(os.path.dirname(__file__))
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(APP_DIR, os.getenv('DATABASE_URI'))
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:HHxxhust568@127.0.0.1/shop"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 获取根级目录
    ROOT_DIR = os.path.dirname(APP_DIR)
    DIST_DIR = os.path.join(ROOT_DIR, 'dist')

    if not os.path.exists(DIST_DIR):
        raise Exception('DIST_DIR not found: {}'.format(DIST_DIR))


app.config.from_object('app.config.Config')
