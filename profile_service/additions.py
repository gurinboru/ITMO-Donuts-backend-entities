from flask_restful import reqparse
from flask_restful import fields

post_parser = reqparse.RequestParser()
post_parser.add_argument('email', type=str, required=True, help="Email is required")
post_parser.add_argument('first_name', type=str, required=True, help="First_name is required")
post_parser.add_argument('second_name', type=str, required=True, help="Second_name is required")
post_parser.add_argument('date_of_birth', type=str)
post_parser.add_argument('phone', type=str)

put_parser = reqparse.RequestParser()
put_parser.add_argument('email', type=str)
put_parser.add_argument('first_name', type=str)
put_parser.add_argument('second_name', type=str)
put_parser.add_argument('date_of_birth', type=str)
put_parser.add_argument('phone', type=str)
put_parser.add_argument('balance', type=int)


user_fields = {
    "id": fields.Integer(attribute="user_id"),
    "email": fields.String,
    "first_name": fields.String,
    "second_name": fields.String,
    "date_of_birth": fields.String,
    "phone": fields.String,
    "balance": fields.Integer
}
