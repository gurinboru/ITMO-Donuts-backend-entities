from flask import Flask
from flask_restful import Api, Resource
from resources import User, Users, Order, Orders


app = Flask(__name__)
api = Api(app)

api_base_url = "/api/v1/profile/"

api.add_resource(User, api_base_url + "user/<int:user_id>")
api.add_resource(Users, api_base_url + "users/")
api.add_resource(Users, api_base_url + "order/<int:order_id>")
api.add_resource(Users, api_base_url + "orders/")

if __name__ == "__main__":
    app.run(debug=True)
