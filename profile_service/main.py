from flask import Flask
from flask_restful import Api, Resource
from resources import User, Users, UserPost, Order, Orders, OrderPost
from middleware import MiddleWare
from kafka.errors import NoBrokersAvailable


try:
    from kafka_consumer import consumer
except NoBrokersAvailable:
    consumer = None
    print("Kafka broker is not available")


app = Flask(__name__)
api = Api(app)

app.wsgi_app = MiddleWare(app.wsgi_app)

api_base_url = "/api/v1/profile/"

api.add_resource(User, api_base_url + "user/<string:username>")
api.add_resource(UserPost, api_base_url + "user")
api.add_resource(Users, api_base_url + "users/")
api.add_resource(Order, api_base_url + "order/<int:order_id>")
api.add_resource(OrderPost, api_base_url + "order")
api.add_resource(Orders, api_base_url + "orders/<int:user_id>")


if __name__ == "__main__":
    if consumer:
        consumer.run()
    app.run(debug=False)
