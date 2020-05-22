from . import api
from .resource import SecureShopResource
from .. import db
from ..models import Item, ItemImage
from flask_restplus import Resource, reqparse
from base64 import b64decode, b64encode

# the number of each group of reviews
GROUP_COUNT = 6

item_post_parser = reqparse.RequestParser()
item_post_parser.add_argument('name', required=True)
item_post_parser.add_argument('original_price', required=True)
item_post_parser.add_argument('current_price', required=True)
item_post_parser.add_argument('in_stock', type=int, required=True)
item_post_parser.add_argument('info', required=True)
item_post_parser.add_argument('item_class', required=True)
item_post_parser.add_argument('images', action='append', required=True)


@api.route('/item/create')
class ItemCreate(SecureShopResource):
    """
    商家发布商品
    URL : /api/item/create
    extra : 需要店铺登录凭证
    method: POST
    args:   (1) name, str, 商品名
            (2) original_price, decimal, 商品原价;
            (3) current_price, decimal, 商品售价;
            (4) in_stock, int, 商品库存;
            (5) info, str, 商品介绍;
            (6) item_class, str, 商品类别
            (7) images, {base64 blob (至少一张)} 数组, 商品图片
    return :(1) 成功, status code 201
                a. item_id, int, 商品id
            (2) 失败, status code 400
                a. message, str, 错误信息
            (3) 权限不足，status code 401
    """
    def post(self, auth_shop):
        args = item_post_parser.parse_args()
        item = Item(shop_id=auth_shop.id,
                    name=args.name,
                    original_price=args.original_price,
                    current_price=args.current_price,
                    in_stock=args.in_stock,
                    info=args.info,
                    item_class=args.item_class,
                    sales=0)
        db.session.add(item)
        db.session.commit()

        # 向数据库中加入图片
        for image in args.images:
            img_data = b64decode(image)
            itemImage = ItemImage(item_id=item.id, image=img_data)
            db.session.add(itemImage)

        db.session.commit()
        return {}, 201


@api.route('/items/<int:item_id>')
class ItemQuery(Resource):
    """
    获取商品信息
    URL : /api/item/:item_id
    method: GET
    args :  (1) item_id, int, 商品id;
    return: (1) 成功, status code 200
                a. current_price, decimal, 商品售价;
                b. original_price, decimal, 商品原价;
                c. in_stock, int, 商品库存;
                d. info, str, 商品介绍;
                e. sales, int, 商品销量
                f. shop_id, int, 商品所属商店id
                g. item_class, str, 商品类别
                h. images, {base64 blob (至少一张)}, 商品图片
            (2) 失败, status code 400
                a. message, str, 错误信息
    """
    def get(self, item_id):
        item = Item.query.get_or_404(item_id)

        item_data = {}
        item_data['shop_id'] = item.shop_id
        item_data['name'] = item.name
        item_data['current_price'] = str(round(item.current_price, 2))
        item_data['original_price'] = str(round(item.original_price, 2))
        item_data['in_stock'] = item.in_stock
        item_data['info'] = item.info
        item_data['sales'] = item.sales
        item_data['item_class'] = item.item_class

        images = []
        for imgRecord in item.images:
            img_data = b64encode(imgRecord.image)
            images.append(img_data.decode('utf-8'))
        item_data['images'] = images

        return item_data, 200


item_put_parser = reqparse.RequestParser()
item_put_parser.add_argument('original_price')
item_put_parser.add_argument('current_price')
item_put_parser.add_argument('in_stock', type=int)
item_put_parser.add_argument('info')
item_put_parser.add_argument('item_class')
item_put_parser.add_argument('images', action='append')


@api.route('/items/<int:item_id>')
class ItemManagement(SecureShopResource):
    def put(self, auth_shop, item_id):
        """
        更新商品信息
        URL : /api/items/:item_id
        extra : 需要店铺登录凭证
        method: PUT
        args :  (1) item_id, int, 商品id;
                (2) original_price(可选), decimal, 商品原价;
                (3) current_price(可选), decimal, 商品原价;
                (4) in_stock(可选), int, 商品库存;
                (5) info(可选), str, 商品介绍;
                (6) item_class(可选), str, 商品类别
                (7) images, {base64 blob (可选)} 数组, 商品图片
        return: (1) 成功, status code 200
                (2) 失败, status code 400
                    a.message, str, 错误信息
                (3) 权限不足，status code 401
        """
        args = item_put_parser.parse_args()
        item = Item.query.get_or_404(item_id)

        item.original_price = args['original_price'] or item.original_price
        item.current_price = args['current_price'] or item.current_price
        item.in_stock = args['in_stock'] or item.in_stock
        item.info = args['info'] or item.info
        item.item_class = args['item_class'] or item.item_class

        # 先删除商品全部图片，再将图片插入
        if args['images']:
            for image in item.images:
                db.session.delete(image)

            for image in args.images:
                img_data = b64decode(image)
                itemImage = ItemImage(item_id=item.id, image=img_data)
                db.session.add(itemImage)

        db.session.commit()
        return {}, 200

    def delete(self, auth_shop, item_id):
        """
        删除商品信息
        URL : /api/items/:item_id
        extra : 需要店铺登录凭证
        method: DELETE
        args :  (1) item_id, int, 商品id;
        return: (1) 成功, status code 200
                (2) 失败， status code 400
                    a. message, str, 错误信息
                (3) 权限不足，status code 401
        """
        item = Item.query.get_or_404(item_id)
        item.deleted = True
        db.session.commit()

        try:
            db.session.delete(item)
            db.session.commit()
        except:
            return {'message': 'Item was used in some order, archived now'}, 200

        return {}, 200


item_search_parser = reqparse.RequestParser()
item_search_parser.add_argument('item_name')
item_search_parser.add_argument('item_class')
item_search_parser.add_argument('rank_type', type=int)
item_search_parser.add_argument('shop_id', type=int)
item_search_parser.add_argument('group_index', type=int)


@api.route('/item/search')
class ItemSearch(Resource):
    """
    搜索商品
    URL : /api/item/search  ?item_name=<item_name>
                            &item_class=<item_class>
                            &rank_type=<rank_type>
                            &shop_id=<shop_id>
                            &group_index=<group_index>
    method: GET
    args :  (1) item_name, int, 商品名称(可选);
            (2) item_class, str, 商品种类(可选);
            (3) rank_type, enum, 排序方式（可选）;
                a. 1, 价格从大到小排序
                b. 2, 价格从小到大排序
                c. 3, 评价从大到小排序
                d. 4, 评价从小到大排序
                e. 5, 销量从大到小排序 （默认）
                f. 6, 销量从小到大排序
            (4) shop_id, int, 店铺id（只搜索该店铺内的商品，可选）
            (5) group_index, int, 组号（可选） 默认为0
    return: (1) 成功, status code 200
                a. item_ids, {int}, 搜索到的商品第index组id集合
            (2) 失败, status code 400
                a. message, str, 错误信息
    """
    def get(self):
        args = item_search_parser.parse_args()
        rank_type = args.rank_type or 5
        group_index = args.group_index or 0
        itemQuery = Item.query.filter_by(deleted=False)

        if args.item_name:
            itemQuery = itemQuery.filter(Item.name.contains(args.item_name))
        if args.item_class:
            itemQuery = itemQuery.filter_by(item_class=args.item_class)
        if args.shop_id:
            itemQuery = itemQuery.filter_by(shop_id=args.shop_id)

        if rank_type == 1:    # 按价格从大到小排序
            itemOrdered = itemQuery.order_by(Item.current_price.desc())
        elif rank_type == 2:    # 按价格从小到大排序
            itemOrdered = itemQuery.order_by(Item.current_price.asc())
        elif rank_type == 3:    # 按评价从大到小排序
            itemOrdered = itemQuery.order_by(Item.average_star.desc())
        elif rank_type == 4:    # 按评价从小到大排序
            itemOrdered = itemQuery.order_by(Item.average_star.asc())
        elif rank_type == 5:    # 按销量从大到小排序
            itemOrdered = itemQuery.order_by(Item.sales.desc())
        elif rank_type == 6:    # 按销量从小到大排序
            itemOrdered = itemQuery.order_by(Item.sales.asc())
        else:
            return {'message': 'Invalid rank type!'}, 400

        total = itemOrdered.count()

        itemsPage = itemOrdered.paginate(page=1 + group_index, per_page=GROUP_COUNT)
        output = []
        for item in itemsPage.items:
            output.append(item.id)

        return {'item_ids': output, 'total': total}, 200


@api.route('/items')
class ItemQueryTest(Resource):
    """获取全部商品信息(测试用)"""
    def get(self):
        items = Item.query.all()

        items_data = []
        for item in items:
            item_data = {}
            item_data['item_id'] = item.id
            item_data['shop_id'] = item.shop_id
            item_data['name'] = item.name
            item_data['current_price'] = str(round(item.current_price, 2))
            item_data['original_price'] = str(round(item.original_price, 2))
            item_data['in_stock'] = item.in_stock
            item_data['info'] = item.info
            item_data['sales'] = item.sales
            item_data['item_class'] = item.item_class
            item_data['deleted'] = str(item.deleted)

            images = []
            for imgRecord in item.images:
                images.append(imgRecord.id)
            item_data['images_id'] = images

            items_data.append(item_data)

        return {'items': items_data}, 200
