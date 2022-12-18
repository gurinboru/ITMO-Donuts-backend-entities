from flask_restful import Resource, marshal_with, abort
from db_methods import dbm
from errors import UsernameAlreadyExists, IdNotFound, UsernameNotFound, EmailAlreadyExists
from werkzeug.exceptions import BadRequest, NotFound
from additions import user_fields, user_post_parser, user_put_parser, order_fields, order_post_parser, order_put_parser


class User(Resource):
    @marshal_with(user_fields)
    def get(self, username):
        try:
            return dbm.get_user(username)
        except UsernameNotFound:
            raise BadRequest("Id not found")

    @marshal_with(user_fields)
    def put(self, username):
        data = user_put_parser.parse_args()
        try:
            return dbm.update_user(username, data)
        except UsernameNotFound:
            raise BadRequest("Id not found")


class UserPost(Resource):
    @marshal_with(user_fields)
    def post(self):
        data = user_post_parser.parse_args()
        try:
            return dbm.add_user(data)
        except UsernameAlreadyExists:
            raise BadRequest("Username already exists")
        except EmailAlreadyExists:
            raise BadRequest("Email already exists")


class Users(Resource):
    @marshal_with(user_fields)
    def get(self):
        return dbm.get_users()


class Order(Resource):
    @marshal_with(order_fields)
    def get(self, order_id):
        try:
            return dbm.get_order(order_id)
        except IdNotFound:
            raise BadRequest("Id not found")

    @marshal_with(order_fields)
    def put(self, order_id):
        data = order_put_parser.parse_args()
        try:
            return dbm.update_order(order_id, data)
        except IdNotFound:
            raise BadRequest("Id not found")


class OrderPost(Resource):
    @marshal_with(order_fields)
    def post(self):
        data = order_post_parser.parse_args()
        return dbm.add_order(data)


class Orders(Resource):
    @marshal_with(order_fields)
    def get(self, username):
        try:
            return dbm.get_orders_by_user(username)
        except IdNotFound:
            raise BadRequest("Username not found")


class HealthCheck(Resource):
    def get(self):
        if dbm.check_db():
            return "OK"
        else:
            raise NotFound("DB is not working")
