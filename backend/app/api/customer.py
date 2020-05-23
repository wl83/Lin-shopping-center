from . import api
from .captcha import check_captcha
from .. import app, db
from ..models import Customer, Gender
from flask_restplus import Resource, reqparse
from flask import request
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from base64 import b64decode, b64encode
import jwt
import datetime

DEFAULT_CUSTOMER_IMG_BASE64 = '''iVBORw0KGgoAAAANSUhEUgAAAIAAAACACAYAAADDPmHLAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAAJOgAACToAYJjBRwAABcuSURBVHhe7Z1pjBRVu8ebAWUGJEaWQUBEGdxAiALJHVEQERckMcGIuIAX4339oryKUZILiAmQ6AcTRaPmunzQi/dVvxgXUHwlcUdlE0RlR9A4LGoUQVHBvvV7up+a0zXV3ae66lQ3yz955pz6n1NVz1Jz6ulaTrXLesgY+PvvvzN1dXX5pRxqnQvi4MGDmVWrVmW2bNmS2bx5s5S7du3K7NmzR8rffvst88cff2QOHDiQadeuXaZjx44inTp1yjQ2NmZ69uwpZVNTU2bAgAEi5513Xua4447L76E40rA3UY4DAHgN2d9//11KRS1yQcC/+eab2WnTpmXPOeccDmZrqatrn/UOgNC2YsI+/vnPadk33ng9r0ErXNjrmpMDgMqvv/7apnHv3r01w/3111/5pWx2xYoV2enTp2d79OjRJkDt2xcGlbr3n5sYF5SuXbtm77777uyHH36Y1y6HKLZVi8OncgCEHRm//PJLTXCKTz/9NDt58uTQICA2wYorNvu46aabRNcgbO1Ni/NOg1Jvd+jQIQyScyHwuIw3GmS6dOlSE9zMmTMzDz74oCwrvCDIeZ72YhgyZEhm8ODBmUGDBmbOPvucTL9+/eS8zvZPPPHEfK9CeI7JtLS0iJA7bNu2LfP1119n1qxZk1m7dm2+VyFK6TJ79uzMvHnzpP7nn39KX5e+suX27duXOeGEE3KcR/godrSkxSk2bdqUveSSSwr+sxBPYfkPDPJnnXVW9q677souWbIk6wUjv5W2YKQzwX4ZGoPwgpWvFQL+7bffln2deeaZbfRQ/ShNfvTo0dmNGzfmt5KMr5Li/APAdgUXnJeRS51z+6mnnlrgvGIyZcoUSf7C4FpnE2+99ZboEqZj8IDFtuXLl+fXbIXtfl1wcgBQCUsSXCug8IbZbP/+/X1Hhf0XIZMn31TgwOB/u+1+k+YU6EYOYOocZge2rl+/Pr+W+wO2GFfVJBDs378ve/HFF/uOCRtCe/XqlX322Wfza+Rgu49qcQCd+/TpU9I2TnP79+/Pr5GD7T7icpoEZkgCbVZIkgMzZ/637wjTQbo8YsSI7Lp16/K9W2G7j2pyXuKVX8pmv/zyS7HFtBUxD4Q5c+bke6czGpijfepJ4I4dO7KdOnUq6ozm5ubsDz/8IH3JDSrZRy1xit27d2cvuOAC387gaNDQ0JDdsGFDvncOtvuIw6WaBM6YMcM3OCinnHKKHBwK17pUi/vmm2+yffueUmC7eSDgI4VrXainkgRShl21U3nttdekH7DZHjhcOf3Fg81qf3A0aGxszHq/1aWfIso+bLlUksBly5b5hplGItdff730UdhsDxwpHJg0aVKBT0wf4Ttgu70onNMkUDFr1iwxJHh9Hlm9enW+Vw5R93EkcJos8pNQ/RIcDWbPniV9TETZRxjnNAlUjB07NtSgMWPG5Hu0Iuo+jkQOXHLJaN9PiPrtsssuy/dIfr+JJoGKvn37iuLB4D/99NP5Hq2Iuo8jldPR4JlnnvH9ZfoPnwKGbpvt2XKJJYGKzp07t1Ee2b59u7Tbbu9o5viloH4zpUuXLvkeOdhurxiXWBKoqKurE0XN4Hfs2FHaqnHB6XDl9BI3vsOH+BKfUsfHijj7SCwJVGjAzeCfccYZ0lbLzxvUOnfmmWf4BwEl0qFD+3xrK2y3Rz2xJFARNuwPGzZM2vg9a7u9Y1whp8CXGnz1r3k6sN1eGFdxEqgIS/hGjRolbSQ2tttzycWB7T5ccYqRI0e28bMmhnHyt1hJYNhPPf3Pr6Xg//vfb2fvu+++7Lhx48RpqqspXKvo3//07Pjx47Pz588PfawL2O43aQ6cf/75bfS+9NLCn9W226MeKwnUizxh5/xqBl/BwyIXXnhhgbNUNFktxyEc5B988EF+q9W7R6E/E/ExeuFzfE999uzZ0hZle7GSwI8//lh2bAa/vr5e2qp1ztf76q+88oroEybqNHMEKMXpMsIdzOATSFH0S5JraKj39VT9iAmw2V6sJJCSHQYv74JqZfscxKCpqcnXJ0qgbTitDx8+XPYF0rAtyAF+Jqo+phw61PqElO32IieB3bt3l52ZTuE2LkqVW9cFBzZv3uzrUiyASXLIt99+K/tWRNE5LgfwueqCfpTERmG7vUhJoN7PN52hl3fLreuCA2vXrvV1sQ1gXE7r33//vegQReckOXwf1Onee++VNpvtRUoCzSNORW/slFvXBXfgwAHhVZdiwXLNgaSvz9tygBioLipcSlYUWzdSEgiCj3EhQYSt64JjtAKqh22wkuYQXg0zEcWOuJxCdUE/Sr38DsLWjZQEgpkzZ/o7UVm1alW+NYewdV1xgJdB0cM2WK446g888IDoFNWOpLivvvrK10n147oHKLeufwCENQJ+1ulGVar5JI/WVRcXQa2EA9X6CQxuuOEGX5dWncqvK5pTCUsCgfncfuuGW0G/pA0qx02cOFH0cB1UWw65447bRTeFjR0gCU6huqAfJa+kgWLrlkwCeXiRN3Z0o2pwLTzAiR4dOnQoG5i0OK6JUFfY2pE0pw+amvpxegh7vL5sEgj0dS3dII9uK7Rf2LouubCfPtTTCHQ57o033hAdXfugGAf05pwKMTRBv7JJIOBFTdNI6vrcvvbTjYA0OGC+XGHqVyowaXHXXHON6FiJbUlwgAtUpn7UiSUIW9c/AIKN+paubgTHg7CNpMUBdFGxDUwanIqJKLYlyemraKpfv379hA9bVzSmYg4LvJ/PiqaRe/bskbYkFY3CceFn69atoosal2QAk+Co69wCUWxLkgM8f6m6qXDF1ATrFE0CdXIGNZIjCrhWvhQHXn75ZV8vFwFMgtNbxy58YMsBPVWqXubj+PQrmQSqcSq8pVsLL2ref//9oo/LAMblnnjiCdE1qm0gSY63ktEH/VQ3hTna13nw548BzMljonfv3plBgwbVxPw2LS3fS3nQmJOHNu8nYU1wwEvCpKQd0ObaL2HcwIEDM3369Ml4w7wsA+YsAv78QMBbWaBHBJQptTI5AwibfaPS/1QXHOWMGbm7ccDWNhcc8vzzz/v6qZigjzBUSAh4Dq7cCmkoH8YB80XKKIFJi6POBFIgim0uOIXqqPp99tlnwtOPmMucod75XYazxx57jEV/ePD+46QEbMv1sFWKA8cff7yUtCU5dCfFAaacBS58EIVTTJkyWUrVb8GCBVIyTS56SxKo8HgRPVp0QqZSR1qa3K233urr5xnt60u9VjjunIKotoGkOfD+++/7uqmYkCQQrFy5UkrPID9xGD58eGJHZBKcjgBx/1NdcUD9STugzbVfSnEjR46UZaBtGmvgTxv9wgsvSIlBYMqUKVK6UKoSDpjtgGXXQY3Cgc6dO0sJaHPtl1Ic2T7QWKIzWLhwoZT044+gsbFwChcegfYMrGjoSZpT6HUAxDPW+XAelaPO692KsFvsrn0VxhFL1ZOyW7duwvtXAoEaoxKE7c6S5kDwmYRSQagFDpkwYUJe+xxs7U2aU5i6IZr7SaT1CFE5++yzpFFhu7OkOeANVwW62QahWhziDbVSmi9ruPZVKQ7o3MaqK1PcAskBFi9eTOGfQ668cpyUwOvj5PxkwwFm7VbQFuccnQbnHRD8spLldevWSZmGr0pxYNy4XEzRGSxatEhKOQDeeecdWdDGq666SkqXStlwoH379lLSFicw1eKop+Grctz48eOlRD+wdOlSKemMtjLpgNdZ6l4naCfDUVTuySefFJ2SHKbT4JAXX3xRbFDY2AuS5sDPP/9coBsC+M0vC6bywLVStpw3OrXRL8zhtcZRckdOYWuvKw4E9ZPYc21YG5AhQ4ZIZ9sNu+RAS0tLgX7FHF5rHHWFrb2uOWKLXqofsa8zkyzAZ1aAZ4iU3nrOz0+luJNPPlmWAW1pnLfjclxJpQ5oc+GXSjg+fQfQGfA5Pf8A0E58Y0eRhlKlOL2S1dzcLKWLYLngwIQJE6R04ZdKONC/f38paQebNm3K1HEUAJQHfGAJJK1AHG7ixIlSugiWK+7aa6/NeEOvU79E4dDl3HPPlWXF1q1b+c1/JRr757GVK1d6/WsnCVSgmwq6xj1Hu+SQIGztdcUB81F/SuZMygwdOrRAcZ4rr9ZMH8U4sHjxYl951wGMwyF6BVAR1V5XnL4zgM6UEnve9jGV5/eiCZsNgzS4BQsWFOiK2AYmDQ5ZuPB/89rmYGtbGlzwJ7/EnvfbTdKE7YbT4sC7774reqrOroNqyyHBT8JFsc01B1g29ZXYm7N8UipsN1wN7uqrr/Z1riRYSXPIbbfdJropbOwAaXHcmgamzt6vrGwdz4ZxvZ0MVkG/NDLTSrlu3bpJmVTGHpcD3bt3lxLQ5toHUTn9SQ1oww4v18vUscDdKzoq9u3bl4pSlXBADwDaAW1JBzUKB3r27Cklba59EIcDageo06dYTbhUIC4H+BC0gra4AYzLgb59+0qZhg8q5RSqc319feawSgLhwNKlS32dXZ/fbblaeX0OhHEK1ReR2OvPQAyi1EeFbDdcDe6nn37yda4kWElziPl4PbCxA6TFMZWu959foLNMAaAXgtSg7777TlZKQ6lKOWAaovq7DnQYh7Rv3/oVD2BrR5ocILZqByWxrzOTF9DS0iJ3s1yei+JyQO9sAdpcnd/LceCKK66QEtCWhg+icmDnzp1SYgcg9nWNjY2yoOAOkXeUp6JUpRyYOnWqlLQlHdQoHLj55v+UkjYX9ibF7dixQ0rsAMS+bsCAAbKgnbZt2yYlSEOpSjhw5513SqnXMGgH9HcR6DCOkRJMmjRJSlf2JsGBtWvXSEk7aGpqaj0AMAisX79eyqQVSJoD//jHf6US6GIcmDt3rpR79+51am9cDmzaVPjwj8Se69de3U8MBg8e7PWv7SSQOrNyAnRW/ZNM7mw54DncSudqcoDYqh2U8jig3iEyBdhuuNrcU089JTq7DnQYt2jRItGjlH6gVjjVGzsovVEs92aQNqhxf/2Vm+kK2GwYVIsDJ510km+D2pFkoMM43rQBlehcDU6C7emNHWoDkL8DBw4saNTXhmw2DKrJMX3cjz/+6BtlG8A4HKKnIEUUnavBLVmyxLeHkpgDeTNo7NixFH5i4x0AUiadiLjgmDOga9eumXnz5gnvKuFTDjz11P/U1Gvg5Tjw+uuvS0k7GDNmjJQQMsctVZXDbXhT9OhR+Iq754DE//MHDcr95yhs9asmB/QTtCreASG8HADAbERMRNlZtTjAd/ZVf9ugRuEop06dKvsCUfSrFueNBlIP2qHwZwjRe+ye4VLqacDr43yISoIDOizT5uJUABoaGqTU/aZhWxyOB0G8879wtMFrrIF/ANx8881SYjjQKWNcKOWCAxqkuIEuxgH9B3FlR9Ic0ClhsAPolDH044/go48+wuICATbDTK1wN954o+jtOcK3gXqcYT/I3X33dNlXJfpVi0Nv80Of+u4H14BkBGCewBEjRlAVeB2lXL58eeJHpCsO6AxdtAPakvjPVw7U1bXOVwBoc21bHG7FihVSegeEtIOhQ4fK84DYV0eDTr+mE0PSAB5++GEpk1bKBQd4wFVBW6WBLsYBvQEEaEvDtko58NBDD0lJO/BGSSnlcTDgNfjQqWK9DUipzd6GKxp60uSA+ZpbksO+ctRvueUW2VdU/dLmFGqDynvvvZdvycE/AHTl4Aq1Mlm0DWde0bQNalTu0ksvlX25tAPE5ZBIk0XriwN8i56OanDPnj2FB/RLQ/lKufr6jkx9WjKAcTn9CFMl+qXJgcbGRt8OSv2YJKCf3AhkIfgyKJ1Nw3niFbhQNCkOmMZqPcngq5iw1S9NDnzxxRcFdph606/oF0PA6NGFEzOaH4xS6M5qgQPPPfdcgc62QY3KUWcCZmCrXzW45uZm0VV15jNAgHZzBtOCwxmSZ9s3btxYYDglc/UogjsD1eLAH38c8PVVneMGuhwHuBNZic6uOZ1XydR58+bN0hZc1z8AghvhU2O6EUqOKBDsB6rFAX6hoJ+KbQDjcEhDQ0NegxxsdU6Da27+D193ysifjQPB2SSQLVu21MzbL+Bf//o/XzfV1XXwldNl/VlVK6PBtm3bfD1VRx7743N2wXWLJoFab2rKfTpWpXfv3sIr6OfaIOVM8A08HaFUSgXLJYcMHnyufNPQhAsflONAnz69C3Qr9qvF6tvBGzZskI2o4dT149HaL2zdJDn+sxQvvfRStlevXgUGmvqVC5YrTpd5jkK/H2wiir2VcuDll1/ydVFZvXp1vjUH1imZBAY3zAcH2ZBpOHB9dVDBV0y5+qb7DupSKjBpc6bcfvvt2Z07d+atKIStD2w5RVAH/Xy8Imzdokmg4rff9rfZ8HXXXZdvzSFs3ahcEHPnzs126tSpYL+uA5g0h3Ax5pFHHslblUMw3yrlFxsOmF9UUzFRbF3pRaWYUkC/1KFGUudCA9B+YevacLy1qnj11Vezw4YNKzDC3G85h9cip8vIqFGj5FFyE1F8FcYdPHgwu2bNmoL9UhIzRbF1SyaBwRUaGuoLdoAAno4tt24YZ+Kee+7xtxmUUs49nLigmAEyYes/6mEvx1DW19cLD4qtWzYJNDmwYcN6f0cqI0eOzLfmELZuse3xk3L8+PEF23MdhFriVCZNuk5GX4WN/5QD+jkd3Qf1HTt2SFuxdSMlgcqBGTNmtNnZ448/Lm2l1jW5Xbt2ZUeMyH3ZWiXMQUcDp8sIs3bu3r0776UcSvkU4Pvg9ogRKLWuyfkHgO0KwTtMCL+BbUaSK6+8wl9HpZSDjiZO6yRzimLxANu3b/fXYXuU3bt3lzZgE0vqZZNAkwOcd3THppjQdRXz58/3+9k442jnkEcffTTvvRyCPtV+rKt1hW3wIyWByoFPPvlEdqjKqyIK7UeGqiNGhw4dyhp+jMtx+Iq6vqAD1KeAdWg31yUmoFjcglykJDCM4+ECVZgS0ZsOgPcLlY/jjKOdQ3hiWyETO3mc2Y+HeIBt8CtKAoMcuPzyy30lVRmyUr6eqXySzjgaOR7nps4l5osuukjqZj/ehgK2cQty/gFgu4JyirAjEilm0DGucg4xOXwPbPK3YpwcAFQq3Qjo0qVLgZK2Bh3jKueY6BlUeiGOekVJYJDTZEKHKhvlj3HxOB58BfjeJkal4lZxEhjGafYa1aBjnD3HPxqI80+bSBIY5BTm6cDGoGOcPafDfpzgB7mKk8AwTnEsMUye04QvzrAfxsVOAsM4wBs0akyYQcc4e05/6sVJ+MK4RJLAMI6DCehbRohLBx2JnC7rRZ4k/0GpO0kCw7hly5b5xqhEdcbRxuly1Mu7tpyTJLAYBzjIzAmcXDjtSOGoV3JXr1Iu0SSwHDdjxr2+wUHDbR10pHJa1/v5wHU8qDtJAsM4BfexeWRJDU7DubXMqeATfZIHJOn7YpyzJNCGmzNnThsn2DrtSOFUbB7gTJpLLQkM40zw1qo6wrXDa4lDbJ7bd8GlmgTacOvXr882NTUVOMfWkYcjd/rpp4e+sePaz2FcqklgMY4XTgHTlwXf+VOxdW4tcrp82mmntfm+MIjiq6S51JJAWw7w8qe+kqbiIjAuOVM4zen7+WFv6br2aTGuqklgKc7ErFmz2jjUNgjV4lTMOXmAC19VylU1CbTlTDB0Tp48uY2TEdvAuOC0rsJspe+/XzgVm629aXFFk0AOhuCpoJY4BbnC9OnTc58+DQQAiRLAKJwum9KtWzfRRadfDSINv8ThCpJAXtQ0G2uRCwKeJ5CnTZuWHTRoUGiQiok5f66tMBfhHXfc4c+3byLsVq0LHyTJtaPiGSbTojI9qonDkQPwn3/+ecZLvORDmFu2bMns3r3bFy/nkfmRKTGfaVP5ijrTzffo0UO+qMlHFfmuHp9WQ5hf1ztg8ntoi6TtSIM7dOhQ5v8B8IXgvmuNJ9MAAAAASUVORK5CYII='''


def require_auth(f):
    """登录请求装饰器"""
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            token = request.headers['Authorization']
            data = jwt.decode(token, app.config['SECRET_KEY'])
            auth_customer = Customer.query.filter_by(id=data['customer_id']).first()
            if not auth_customer:
                raise Exception('Wrong customer id')
        except:
            return {
                'message': 'This request needs correct access token!'
            }, 401, {
                'WWW-Authenticate': 'Basic realm : "Login required!"'
            }
        kwargs['auth_customer'] = auth_customer
        return f(*args, **kwargs)

    return decorated


customer_login_parser = reqparse.RequestParser()
customer_login_parser.add_argument('phone', required=True)
customer_login_parser.add_argument('password', required=True)


@api.route('/customer/login')
class CustomerLogin(Resource):
    """
    用户登录
    URL : /api/customer/login
    method : GET
     args:  (1) phone , str, 用户手机号;
            (2) password, str, 密码;
     return:(1) 成功，status code 200
                a. token, str, 验证用token
            (2) 信息错误，status code 400/401
                a. message, str, 错误信息
    """
    def get(self):
        auth = customer_login_parser.parse_args()
        if not auth.phone or not auth.password:
            return {'message': 'Bad login request!'}, 400

        user = Customer.query.filter_by(phone=auth.phone).first()
        if user:
            if check_password_hash(user.password_hash, auth.password):
                token = jwt.encode(
                    {
                        'customer_id': user.id,
                        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60)
                    }, app.config['SECRET_KEY'])
                token = token.decode('UTF-8')
                return {'token': token}, 200

        return {'message': 'Wrong phone or password!'}, 401


customer_reg_parser = reqparse.RequestParser()
customer_reg_parser.add_argument('phone', required=True)
customer_reg_parser.add_argument('password', required=True)
customer_reg_parser.add_argument('nickname', required=True)
customer_reg_parser.add_argument('gender', type=int, required=True)
# customer_reg_parser.add_argument('captcha_identifer', required=True)
# customer_reg_parser.add_argument('captcha_code', required=True)
customer_reg_parser.add_argument('image')


@api.route('/customer/register')
class CustomerRegister(Resource):
    """
    用户注册
    URL : /api/customer/register
    method : POST
    args:   (1) phone , str, 用户手机号;
            (2) password, str, 密码;
            (3) nickname, str, 昵称;
            (4) gender, int, 性别枚举值;
            (5) payment_info, str, 付款方式;
            (6) image（可选）, base64 img, 头像;
            (7) captcha_identifer, str, 验证码标识;
            (8) captcha_code, str, 用户输入的验证码;
    return: (1) 成功，status code 201
            (2) 失败，status code 400
                a. message, str, 错误信息
    """
    def post(self):
        args = customer_reg_parser.parse_args()

        # 检查验证码
        # if not check_captcha(args.captcha_identifer, args.captcha_code):
        #     return {'message': 'Wrong captcha code!'}, 400

        if args.gender == Gender.male.value:
            gender = Gender.male
        elif args.gender == Gender.female.value:
            gender = Gender.female
        else:
            gender = Gender.unknown

        password_hash = generate_password_hash(args.password)
        new_user = Customer(phone=args.phone,
                            password_hash=password_hash,
                            gender=gender,
                            name=args.nickname)

        # 储存用户头像
        if args.image:
            new_user.image = b64decode(args.image)

        # 如果用户已经存在，返回400错误
        try:
            db.session.add(new_user)
            db.session.commit()
        except:
            return {'message': 'Phone already exist! Please login.'}, 400

        return {}, 201


@api.route('/customer')
class CustomerManagement(Resource):
    """
    获取用户信息（带验证）
    URL : /api/customer
    method : GET
    args: 无
    extra : 需要用户登录凭证
    return: (1) 成功，status code 200
                a. customer_id, str, 顾客id;
                b. phone, str, 手机号;
                c. nickname, str, 昵称;
                d. gender, int, 性别枚举值;
                e. payment_info, str, 付款方式;
                f. created_time, str, 创建时间;
                g. image, base64 img, 头像;
            (2) 信息错误，status code 400
                a. message, str, 错误信息
            (3) 权限不足，status code 401
    """
    method_decorators = [require_auth]

    def get(self, auth_customer):
        data = {}
        data['customer_id'] = auth_customer.id
        data['nickname'] = auth_customer.name
        data['phone'] = auth_customer.phone
        data['gender'] = auth_customer.gender.value
        data['payment_info'] = auth_customer.payment_info
        data['created_time'] = str(auth_customer.created_time)
        if auth_customer.image:
            data['image'] = b64encode(auth_customer.image).decode('utf-8')
        else:
            data['image'] = DEFAULT_CUSTOMER_IMG_BASE64
        return data, 200


@api.route('/customer/<int:customer_id>')
class CustomerQuery(Resource):
    def get(self, customer_id):
        """
        获取用户信息
        URL : /api/customer/:customer_id
        method : GET
        args:   (1) customer_id, str, 顾客id;
        return: (1) 成功，status code 200
                    a. nickname, str, 昵称;
                    b. gender, int, 性别枚举值;
                    c. phone, str, 手机号;
                    d. image, base64 img, 头像;
                (2) 信息错误，status code 400/404
                    a. message, str, 错误信息
        """
        """返回一个用户信息(测试用)"""
        customer = Customer.query.get_or_404(customer_id)

        data = {}
        data['nickname'] = customer.name
        data['gender'] = customer.gender.value
        data['phone'] = customer.phone
        if customer.image:
            data['image'] = b64encode(customer.image).decode('utf-8')
        else:
            data['image'] = DEFAULT_CUSTOMER_IMG_BASE64
        return data, 200

    def delete(self, customer_id):
        """删除一个用户信息(测试用)"""
        customer = Customer.query.get_or_404(customer_id)

        db.session.delete(customer)
        db.session.commit()
        return {}, 200


@api.route('/customer/test')
class CustoemrTest(Resource):
    """返回所有用户信息(测试用)"""
    def get(self):
        customers = Customer.query.all()
        data = {}
        output = []
        for customer in customers:
            data['customer_id'] = customer.id
            data['name'] = customer.name
            data['phone'] = customer.phone
            data['password_hash'] = customer.password_hash
            data['gender'] = str(customer.gender)
            data['payment_info'] = customer.payment_info
            data['created_time'] = str(customer.created_time)
            output.append(data.copy())
        return {'customers': output}, 200
