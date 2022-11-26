from flask import Flask
import sqlalchemy.ext.declarative as dec
from sqlalchemy.orm import Session
from sqlalchemy import orm

import sqlalchemy as sa


SqlAlchemyBase = dec.declarative_base()


class DataBase:
    def __init__(self, conn_str):
        from db_models import Users, Orders, OrdersToProducts

        engine = sa.create_engine(conn_str, echo=False)
        self.factory = orm.sessionmaker(bind=engine)

        SqlAlchemyBase.metadata.create_all(engine)

    def get_session(self):
        return self.factory(expire_on_commit=False)
