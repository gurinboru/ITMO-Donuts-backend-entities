import sqlalchemy as sa
from sqlalchemy import orm
from db_session import SqlAlchemyBase


class Users(SqlAlchemyBase):
    __tablename__ = 'users'

    user_id = sa.Column(sa.Integer, primary_key=True, nullable=False)
    email = sa.Column(sa.String(80), unique=True)
    first_name = sa.Column(sa.String(30))
    second_name = sa.Column(sa.String(30))
    date_of_birth = sa.Column(sa.Date)
    phone = sa.Column(sa.String(14))
    balance = sa.Column(sa.Integer, default=10000)
    orders = orm.relationship('Orders', backref='Users')

    def __repr__(self):
        return f"Users(user_id={self.user_id}, " \
               f"email={self.email}, " \
               f"first_name={self.first_name}, " \
               f"second_name={self.second_name}, "


class Orders(SqlAlchemyBase):
    __tablename__ = 'orders'

    order_id = sa.Column(sa.Integer, primary_key=True, nullable=False)
    user_id = sa.Column(sa.Integer, sa.ForeignKey('users.user_id'))
    order_date = sa.Column(sa.Date)
    status = sa.Column(sa.Integer, default=0)
    products = orm.relationship('OrdersToProducts', backref='Orders')


class OrdersToProducts(SqlAlchemyBase):
    __tablename__ = 'orders_to_products'

    id = sa.Column(sa.Integer, primary_key=True)
    order_id = sa.Column(sa.Integer, sa.ForeignKey('orders.order_id'))
    product_id = sa.Column(sa.Integer, nullable=False)
