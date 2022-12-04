from db_models import Users, Orders, OrdersToProducts
from db_session import DataBase
from errors import UsernameAlreadyExists, UsernameNotFound, IdNotFound

import os


class DBMethods:
    def __init__(self, conn_str):
        self.db = DataBase(conn_str)

    def get_user(self, username):
        session = self.db.get_session()
        result = session.query(Users).filter(Users.username == username).first()
        if not result:
            raise IdNotFound
        return result

    def add_user(self, data: dict):
        session = self.db.get_session()

        if session.query(Users).filter(Users.username == data.get("username")).first():
            raise UsernameAlreadyExists

        new_user = Users()

        new_user.username = data.get("username")
        new_user.email = data.get("email"),
        new_user.first_name = data.get("first_name"),
        new_user.second_name = data.get("second_name"),
        new_user.date_of_birth = data.get("date_of_birth"),
        new_user.phone = data.get("phone")

        session.add(new_user)
        session.commit()

        return new_user

    def update_user(self, username, data):
        session = self.db.get_session()

        user = session.query(Users).filter(Users.username == username).first()

        if not user:
            raise IdNotFound

        user.email = data.get("email") or user.email,
        user.email = data.get("username") or user.username,
        user.first_name = data.get("first_name") or user.first_name,
        user.second_name = data.get("second_name") or user.second_name,
        user.date_of_birth = data.get("date_of_birth") or user.date_of_birth,
        user.phone = data.get("phone") or user.phone
        user.balance = data.get("balance") if data.get("balance") is not None else user.balance

        session.commit()

        return user

    def get_users(self):
        session = self.db.get_session()
        result = session.query(Users).all()
        return result

    def add_order(self, data: dict):
        session = self.db.get_session()
        new_order = Orders()

        new_order.user_id = data.get("user_id")
        new_order.order_date = data.get("order_date")
        new_order.status = data.get("status")

        for el in data.get("products"):
            new_order_to_product = OrdersToProducts()
            new_order_to_product.product_id = el
            new_order.products.append(new_order_to_product)

        session.add(new_order)
        session.commit()
        return new_order

    def update_order(self, order_id, data):
        session = self.db.get_session()
        order = session.query(Orders).filter(Orders.order_id == order_id).first()

        if not order:
            raise IdNotFound

        order.status = data.get("status") if data.get("status") is not None else order.status

        session.commit()
        return order

    def get_order(self, order_id):
        session = self.db.get_session()
        result = session.query(Orders).filter(Orders.order_id == order_id).first()
        if not result:
            raise IdNotFound
        return result

    def get_orders_by_user(self, user_id):
        session = self.db.get_session()
        result = session.query(Orders).filter(Orders.user_id == user_id).all()
        if not result:
            raise IdNotFound
        return result


db_login = os.getenv("DB_LOGIN")
db_password = os.getenv("DB_PASSWORD")
db_ip = os.getenv("DB_IP")
db_port = os.getenv("DB_PORT")


if db_ip and db_port and db_login and db_password:
    dbm = DBMethods(f"mysql://{db_login}:{db_password}@{db_ip}:{db_port}/donuts_profile")
else:
    raise Exception("You need to set environment variables DB_LOGIN, DB_PASSWORD, DB_IP and DB_PORT")

