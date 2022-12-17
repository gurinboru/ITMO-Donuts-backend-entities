from db_models import Users, Orders, OrdersToProducts
from db_session import DataBase
from errors import UsernameAlreadyExists, UsernameNotFound, IdNotFound, EmailAlreadyExists
from sqlalchemy.exc import OperationalError

import os
from dotenv import load_dotenv

load_dotenv()


class DBMethods:
    def __init__(self, conn_str):
        self.db = DataBase(conn_str)

    def get_user(self, username):
        session = self.db.get_session()
        result = session.query(Users).filter(Users.username == username).first()
        if not result:
            raise UsernameNotFound
        return result

    def add_user(self, data: dict):
        session = self.db.get_session()

        if session.query(Users).filter(Users.username == data.get("username")).first():
            raise UsernameAlreadyExists
        if session.query(Users).filter(Users.email == data.get("email")).first():
            raise EmailAlreadyExists

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
            raise UsernameNotFound

        user.email = data.get("email") or user.email,
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

        for product in data.get("order_items"):
            new_order.products.append(OrdersToProducts(product_id=product.get("product_id"),
                                                       count=product.get("count")))

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

    def get_orders_by_user(self, username):
        session = self.db.get_session()
        user = session.query(Users).filter(Users.username == username).first()
        if not user:
            raise UsernameNotFound
        return user.orders

    def check_db(self) -> bool:
        try:
            self.db.get_session()
            return True
        except OperationalError:
            return False


db_login = os.getenv("DB_LOGIN")
db_password = os.getenv("DB_PASSWORD")
db_ip = os.getenv("DB_IP")
db_port = os.getenv("DB_PORT")


if db_ip and db_port and db_login and db_password:
    dbm = DBMethods(f"mysql://{db_login}:{db_password}@{db_ip}:{db_port}/donuts_profile")
else:
    print(f"DB connection error: {db_ip}, {db_port}, {db_login}, {db_password}")
    raise Exception("You need to set environment variables DB_LOGIN, DB_PASSWORD, DB_IP and DB_PORT")
