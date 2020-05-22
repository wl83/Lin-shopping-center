from .. import app
from . import api
from flask_restplus import Resource, fields
from captcha.image import ImageCaptcha
from base64 import b64encode
from string import ascii_uppercase, digits
from random import choice
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

captcha_image = ImageCaptcha()
chars = ascii_uppercase + digits
LENGTH = 5

s = Serializer(app.config["SECRET_KEY"], expires_in=1200)


@api.route('/captcha')
class Captcha(Resource):
    """
        用户注册验证码获取
        args: 无
        return:
            (1) identifer, str, 验证码标识
            (2) img, base64 img, 验证码图像;
    """
    @api.response(200, "成功", api.model("验证码", {
        'identifer': fields.String,
        'img': fields.String
    }))
    def get(self):
        random_str = ''.join([choice(chars) for i in range(LENGTH)])
        img_data = captcha_image.generate(random_str).read()

        base64_bytes = b64encode(img_data)
        base64_str = base64_bytes.decode('utf-8')

        dump = s.dumps({'code' : random_str})
        dump_str = dump.decode('utf-8')

        return {'identifer': dump_str, 'img': base64_str}


def check_captcha(identider, code):
    """验证用户输入的验证码是否正确(大小写无关)"""

    try:
        data = s.loads(identider)
        return data['code'] == code.upper()
    except:
        return False
