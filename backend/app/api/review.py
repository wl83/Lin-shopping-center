from . import api
from .resource import SecureCustomerResource
from .. import db
from ..models import Review
from flask import request
from flask_restplus import Resource, reqparse

# the number of each group of reviews
GROUP_COUNT = 3

review_post_parser = reqparse.RequestParser()
review_post_parser.add_argument('item_id', type=int, required=True)
review_post_parser.add_argument('star', type=int, required=True)
review_post_parser.add_argument('remark', required=True)


@api.route('/review/create')
class ReviewCreate(SecureCustomerResource):
    """
    保存新的评价
    URL : /api/review/create
    extra : 需要用户登录凭证
    method: POST
    args :  (1) item_id, int, 商品id
            (2) star, int, 评价级别
            (3) remark, str, 评价信息
    return: (1) 成功，status code 201
            (2) 失败，status code 400
                a. message, str, 错误信息
            (3) 权限不足，status code 401
    """
    def post(self, auth_customer):
        args = review_post_parser.parse_args()
        new_review = Review(customer_id=auth_customer.id,
                            item_id=args.item_id,
                            star=args.star,
                            remark=args.remark)

        db.session.add(new_review)
        db.session.commit()
        return {}, 201


@api.route('/review/<int:review_id>')
class ReviewQuery(Resource):
    """
    获取评价信息
    URL : /api/review/:review_id
    method: GET
    args :  (1) review_id, int, 评价id;
    return: (1) 成功，status code 200
                a. remark, str, 评价信息
                b. star, int, 评价级别
                c. created_time, str, 创建时间
                d. customer_id, int, 用户id
                e. item_id, int, 商品id
            (2) 失败，status code 400
                a. message, str, 错误信息
    """
    def get(self, review_id):
        review = Review.query.filter_by(id=review_id).first_or_404()

        remark_data = {}
        remark_data['remark'] = review.remark
        remark_data['star'] = review.star
        remark_data['created_time'] = str(review.created_time)
        remark_data['customer_id'] = review.customer_id
        remark_data['item_id'] = review.item_id
        return remark_data, 200


@api.route('/review/<int:review_id>')
class ReviewManagement(SecureCustomerResource):
    """
    删除评论
    URL : /api/review/:review_id
    extra : 需要用户登录凭证
    method: DELETE
    args :  (1) review_id, int, 评价id;
    return: (1) 成功, status code 200
            (2) 失败, status code 400
                a. message, str, 错误信息
            (3) 权限不足，status code 401
    """
    def delete(self, auth_customer, review_id):
        review = Review.query.get_or_404(review_id)
        db.session.delete(review)
        db.session.commit()
        return {}, 200


review_search_parser = reqparse.RequestParser()
review_search_parser.add_argument('item_id', type=int)
review_search_parser.add_argument('customer_id', type=int)
review_search_parser.add_argument('group_index', type=int)


@api.route('/review/search')
class ReviewSearch(Resource):
    """
    URL : /api/review/search
    method: GET
    args :  (1) item_id（可选）, int, 商品id
            (2) customer_id（可选）, int, 商品id
            (2) group_index, int, 组号, 默认为0
    return: (1) 成功，status code 200
                a. review_ids, {int}, 某商品的第index组评价信息id集合
            (2) 失败，status code 400
                a. message, str, 错误信息
    """
    def get(self):
        args = review_search_parser.parse_args()
        group_index = args.group_index or 0

        reviewQuery = Review.query
        if args.item_id:
            reviewQuery = reviewQuery.filter_by(item_id=args.item_id)
        if args.customer_id:
            reviewQuery = reviewQuery.filter_by(customer_id=args.customer_id)

        total = reviewQuery.count()

        reviews = reviewQuery.paginate(page=1 + group_index, per_page=GROUP_COUNT)
        output = []
        for review in reviews.items:
            output.append(review.id)

        return {'review_ids': output, 'total':total}, 200
