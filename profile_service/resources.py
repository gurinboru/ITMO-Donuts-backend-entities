from flask_restful import Resource, marshal_with, abort
from db_methods import DBMethods
from errors import EmailAlreadyExists, IdNotFound
from werkzeug.exceptions import BadRequest
from additions import user_fields, post_parser, put_parser

import os


db_login = os.getenv("DB_LOGIN")
db_password = os.getenv("DB_PASSWORD")
db_ip = os.getenv("DB_IP")
db_port = os.getenv("DB_PORT")


if db_ip and db_port and db_login and db_password:
    dbm = DBMethods(f"mysql://{db_login}:{db_password}@{db_ip}:{db_port}/donuts_profile")
else:
    print(db_ip, db_port, db_login, db_password)
    raise Exception("You need to set environment variables DB_LOGIN, DB_PASSWORD, DB_IP and DB_PORT")


class User(Resource):
    @marshal_with(user_fields)
    def get(self, user_id):
        try:
            return dbm.get_user(user_id)
        except IdNotFound:
            raise BadRequest("Id not found")

    @marshal_with(user_fields)
    def put(self, user_id):
        args = put_parser.parse_args()
        try:
            return dbm.update_user(user_id, args)
        except IdNotFound:
            raise BadRequest("Id not found")


class Users(Resource):
    @marshal_with(user_fields)
    def get(self):
        return dbm.get_users()

    @marshal_with(user_fields)
    def post(self):
        args = post_parser.parse_args()
        try:
            return dbm.add_user(args)
        except EmailAlreadyExists:
            raise BadRequest("That email address already exists")


class Order(Resource):
    def get(self, order_id):
        pass

    def put(self, order_id):
        pass


class Orders(Resource):
    def get(self):
        pass

    def post(self):
        pass
