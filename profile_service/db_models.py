import sqlalchemy as sa
from sqlalchemy import orm
from db_session import SqlAlchemyBase


class Users(SqlAlchemyBase):
    __tablename__ = 'users'

    user_id = sa.Column(sa.Integer, primary_key=True, nullable=False)
    username = sa.Column(sa.String(80), unique=True)
    email = sa.Column(sa.String(80), unique=True)
    first_name = sa.Column(sa.String(30))
    second_name = sa.Column(sa.String(30))
    date_of_birth = sa.Column(sa.Date)
    phone = sa.Column(sa.String(14))
    balance = sa.Column(sa.Integer, default=10000)
    orders = orm.relationship('Orders', backref='Users')

    def __repr__(self):
        return f'<User> {self.user_id} ' \
               f'{self.username} ' \
               f'{self.email} ' \
               f'{self.first_name} ' \
               f'{self.second_name} ' \
               f'{self.date_of_birth} ' \
               f'{self.phone} ' \
               f'{self.balance}'


class Orders(SqlAlchemyBase):
    __tablename__ = 'orders'

    order_id = sa.Column(sa.Integer, primary_key=True, nullable=False)
    user_id = sa.Column(sa.Integer, sa.ForeignKey('users.user_id'))
    order_date = sa.Column(sa.Date)
    status = sa.Column(sa.Integer, default=0)
    products = orm.relationship('OrdersToProducts', backref='Orders')

    def __repr__(self):
        return f'<Order> {self.order_id} ' \
               f'{self.user_id} ' \
               f'{self.order_date} ' \
               f'{self.status} ' \
                f'{self.products}'


class OrdersToProducts(SqlAlchemyBase):
    __tablename__ = 'orders_to_products'

    id = sa.Column(sa.Integer, primary_key=True)
    order_id = sa.Column(sa.Integer, sa.ForeignKey('orders.order_id'))
    product_id = sa.Column(sa.Integer, nullable=False)
    count = sa.Column(sa.Integer, nullable=False, default=1)

    def __repr__(self):
        return f'<OrderToProduct> {self.id} ' \
               f'{self.order_id} ' \
               f'{self.product_id}'
