from flask_restful import Resource, marshal_with, abort
from db_methods import dbm
from errors import UsernameAlreadyExists, IdNotFound
from werkzeug.exceptions import BadRequest
from additions import user_fields, user_post_parser, user_put_parser, order_fields, order_post_parser, order_put_parser


class User(Resource):
    @marshal_with(user_fields)
    def get(self, user_id):
        try:
            return dbm.get_user(user_id)
        except IdNotFound:
            raise BadRequest("Id not found")

    @marshal_with(user_fields)
    def put(self, user_id):
        data = user_put_parser.parse_args()
        try:
            return dbm.update_user(user_id, data)
        except IdNotFound:
            raise BadRequest("Id not found")


class UserPost(Resource):
    @marshal_with(user_fields)
    def post(self):
        data = user_post_parser.parse_args()
        try:
            return dbm.add_user(data)
        except UsernameAlreadyExists:
            raise BadRequest("Username already exists")


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


class Orders(Resource):
    @marshal_with(order_fields)
    def post(self):
        data = order_post_parser.parse_args()
        return dbm.add_order(data)


class OrderPost(Resource):
    @marshal_with(order_fields)
    def post(self):
        data = order_post_parser.parse_args()
        return dbm.add_order(data)


class OrdersByUser(Resource):
    @marshal_with(order_fields)
    def get(self, username):
        try:
            return dbm.get_orders_by_user(username)
        except IdNotFound:
            raise BadRequest("Id not found")
