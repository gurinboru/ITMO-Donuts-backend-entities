from flask_restful import reqparse
from flask_restful import fields

user_post_parser = reqparse.RequestParser()
user_post_parser.add_argument("username", type=str, required=True, help="Username is required")
user_post_parser.add_argument('email', type=str)
user_post_parser.add_argument('first_name', type=str)
user_post_parser.add_argument('second_name', type=str)
user_post_parser.add_argument('date_of_birth', type=str)
user_post_parser.add_argument('phone', type=str)

user_put_parser = reqparse.RequestParser()
user_put_parser.add_argument('email', type=str)
user_put_parser.add_argument('first_name', type=str)
user_put_parser.add_argument('second_name', type=str)
user_put_parser.add_argument('date_of_birth', type=str)
user_put_parser.add_argument('phone', type=str)
user_put_parser.add_argument('balance', type=int)

order_post_parser = reqparse.RequestParser()
order_post_parser.add_argument('user_id', type=int, required=True, help="User_id is required")
order_post_parser.add_argument('order_date', type=str, required=True, help="Order_date is required")

order_put_parser = reqparse.RequestParser()
order_put_parser.add_argument('order_status', type=str)


user_fields = {
    "id": fields.Integer(attribute="user_id"),
    "email": fields.String,
    "first_name": fields.String,
    "second_name": fields.String,
    "date_of_birth": fields.String,
    "phone": fields.String,
    "balance": fields.Integer
}

order_fields = {
    "id": fields.Integer(attribute="order_id"),
    "user_id": fields.Integer,
    "order_date": fields.String,
    "status": fields.String,
    "products": fields.List(fields.Nested({
        "id": fields.Integer(attribute="product_id"),
    }))
}
