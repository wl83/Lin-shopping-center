from flask import Flask, current_app, send_file
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
import os

app = Flask(__name__, static_folder='../../dist/static', template_folder='../../dist')

# 导入环境变量,密钥等配置
from .config import Config
app.logger.info('ENV >>> {}'.format(Config.FLASK_ENV))
app.logger.info('DB >>> {}'.format(Config.SQLALCHEMY_DATABASE_URI))
app.logger.info('DIST >>> {}'.format(Config.DIST_DIR))

# 初始化 SQL 数据库 ORM
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from . import models    # NOQA

# 允许跨域请求（调试用）
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

# 导入 API blueprint
from .api import api_bp
app.register_blueprint(api_bp)


# 静态站点入口
@app.route('/icon.png', defaults={'path': 'icon.png', 'prefix': ''})
@app.route('/favicon.png', defaults={'path': 'favicon.png', 'prefix': ''})
@app.route('/', defaults={'path': 'index.html', 'prefix': ''})
@app.route('/css/<path:path>', defaults={'prefix': 'css'})
@app.route('/js/<path:path>', defaults={'prefix': 'js'})
def index_client(prefix, path):
    path = os.path.join(prefix, path)
    entry = os.path.join(current_app.config['DIST_DIR'], path)

    return send_file(entry)
