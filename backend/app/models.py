from app import db
from enum import Enum
from datetime import datetime
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy import select, func


class Gender(Enum):
    unknown = 0
    male = 1
    female = 2


class Status(Enum):
    pending = 0
    payed = 1
    delivering = 2
    arrived = 3
    confirmed = 4
    abnormal = 5


class CartItem(db.Model):
    __tablename__ = 'customer_item'

    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'), primary_key=True)
    selected = db.Column(db.Boolean, nullable=False)
    count = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<CartItem customer_id,item_id:{},{}>'.format(self.customer_id, self.item_id)


class Customer(db.Model):
    __tablename__ = 'customer'

    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(12), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    name = db.Column(db.String(30), nullable=False)
    gender = db.Column(db.Enum(Gender), nullable=False)
    payment_info = db.Column(db.String(100))
    created_time = db.Column(db.Date, default=datetime.utcnow)
    image = db.Column(db.LargeBinary)

    addresses = db.relationship('Address', backref='customer')
    orders = db.relationship('Order', backref='customer')
    reviews = db.relationship('Review', backref='customer')
    cartItems = db.relationship('CartItem', backref='customer')

    def __repr__(self):
        return '<Customer id:{}, {}>'.format(self.id, self.name)


class Address(db.Model):
    __tablename__ = 'address'

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    receiver = db.Column(db.String(30), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    deleted = db.Column(db.Boolean, nullable=False, default=False)

    orders = db.relationship('Order', backref='address')

    def __repr__(self):
        return '<Address customer_id:{}, {}>'.format(self.customer_id, self.receiver)


class OrderItem(db.Model):
    __tablename__ = 'order_item'

    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'), primary_key=True)
    amount = db.Column(db.Integer, nullable=False)
    price_paid = db.Column(db.DECIMAL, nullable=False)

    def __repr__(self):
        return '<OrderItem order_id,item_id:{},{}>'.format(self.order_id, self.item_id)


class Order(db.Model):
    __tablename__ = 'order'

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'), nullable=False)
    status = db.Column(db.Enum(Status), nullable=False)
    created_time = db.Column(db.Date, default=datetime.utcnow)
    payment_time = db.Column(db.Date, default=datetime.utcnow)
    payment_amount = db.Column(db.DECIMAL, nullable=False)

    items = db.relationship('OrderItem', backref='order')

    def __repr__(self):
        return '<Order customer_id:{}, id:{}>'.format(self.customer_id, self.id)


class Review(db.Model):
    __tablename__ = 'review'

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'), nullable=False)
    star = db.Column(db.Integer, nullable=False)
    remark = db.Column(db.Text, nullable=False)
    created_time = db.Column(db.Date, default=datetime.utcnow)

    def __repr__(self):
        return '<Review customer_id,item_id:{},{}, id:{}>'.format(self.customer_id, self.item_id,
                                                                  self.id)


class Item(db.Model):
    __tablename__ = 'item'

    id = db.Column(db.Integer, primary_key=True)
    shop_id = db.Column(db.Integer, db.ForeignKey('shop.id'), nullable=False)
    name = db.Column(db.String(50), index=True, nullable=False)
    original_price = db.Column(db.DECIMAL)
    current_price = db.Column(db.DECIMAL, nullable=False)
    sales = db.Column(db.Integer, nullable=False)
    in_stock = db.Column(db.Integer, nullable=False)
    info = db.Column(db.Text, nullable=False)
    item_class = db.Column(db.String(20), nullable=False, default="未分类")
    deleted = db.Column(db.Boolean, nullable=False, default=False)

    orders = db.relationship('OrderItem', backref='item')
    reviews = db.relationship('Review', backref='item')
    images = db.relationship('ItemImage', backref='item')

    @hybrid_property
    def average_star(self):
        # return db.session.query(func.avg(Review.star).label('avg_star')).filter_by(id=self.id)
        if (len(self.reviews) == 0):
            return None
        return sum(review.star for review in self.reviews) / len(self.reviews)

    @average_star.expression
    def average_star(cls):
        return select([func.avg(Review.star)]).where(Review.id == cls.id).label('avg_star')

    def __repr__(self):
        return '<Item id:{}, {}>'.format(self.id, self.name)


class Shop(db.Model):
    __tablename__ = 'shop'

    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(20), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    name = db.Column(db.String(80), index=True, nullable=False)
    address = db.Column(db.String(200), nullable=False)
    info = db.Column(db.Text, nullable=False)
    created_time = db.Column(db.Date, default=datetime.utcnow)

    items = db.relationship('Item', backref='shop')

    def __repr__(self):
        return '<Shop id:{}, {}>'.format(self.id, self.name)


class ItemImage(db.Model):
    __tablename__ = 'item_image'

    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'), nullable=False)
    image = db.Column(db.LargeBinary, nullable=False)

    def __repr__(self):
        return '<ItemImage item_id:{}, id:{}>'.format(self.item_id, self.id)
