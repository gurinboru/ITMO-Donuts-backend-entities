from flask_restful import reqparse
from flask_restful import fields
from flask_restful import inputs

user_post_parser = reqparse.RequestParser()
user_post_parser.add_argument("username", type=str, required=True, help="Username is required")
user_post_parser.add_argument('email', type=str)
user_post_parser.add_argument('first_name', type=str)
user_post_parser.add_argument('second_name', type=str)
user_post_parser.add_argument('date_of_birth', type=inputs.date, help="Date of birth must be in format YYYY-MM-DD")
user_post_parser.add_argument('phone', type=str)

user_put_parser = reqparse.RequestParser()
user_put_parser.add_argument('email', type=str)
user_put_parser.add_argument('first_name', type=str)
user_put_parser.add_argument('second_name', type=str)
user_put_parser.add_argument('date_of_birth', type=inputs.date, help="Date of birth must be in format YYYY-MM-DD")
user_put_parser.add_argument('phone', type=str)
user_put_parser.add_argument('balance', type=int)

order_post_parser = reqparse.RequestParser()
order_post_parser.add_argument('user_id', type=int, required=True, help="User_id is required")
order_post_parser.add_argument('order_date_time', type=inputs.datetime_from_iso8601,
                               help="Datetime must be in format YYYY-MM-DDTHH:MM:SS (ISO8601)")
order_post_parser.add_argument('order_items', type=dict, required=True,
                               help="order_items should be a list of dict with keys: product_id, count",
                               action='append')

order_put_parser = reqparse.RequestParser()
order_put_parser.add_argument('order_status', type=str)


user_fields = {
    "id": fields.Integer(attribute="user_id"),
    "username":  fields.String,
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
        "count": fields.Integer
    }))
}
