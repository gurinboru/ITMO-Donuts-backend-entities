from db_models import Users, Orders, OrdersToProducts
from flask_sqlalchemy import SQLAlchemy
from db_session import DataBase
from errors import EmailAlreadyExists, IdNotFound


class DBMethods:
    def __init__(self, conn_str):
        self.db = DataBase(conn_str)

    def get_user(self, user_id):
        session = self.db.get_session()
        result = session.query(Users).filter(Users.user_id == user_id).first()
        if not result:
            raise IdNotFound
        return result

    def add_user(self, data: dict):
        session = self.db.get_session()

        if session.query(Users).filter(Users.email == data.get("email")).first():
            raise EmailAlreadyExists

        new_user = Users()

        new_user.email = data.get("email"),
        new_user.first_name = data.get("first_name"),
        new_user.second_name = data.get("second_name"),
        new_user.date_of_birth = data.get("date_of_birth"),
        new_user.phone = data.get("phone")

        session.add(new_user)
        session.commit()

        return new_user

    def update_user(self, user_id, data):
        session = self.db.get_session()

        user = session.query(Users).filter(Users.user_id == user_id).first()

        if not user:
            raise IdNotFound

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
