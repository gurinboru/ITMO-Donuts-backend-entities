from flask_kafka import FlaskKafka
from threading import Event
from db_methods import dbm
from json import loads
from logging import getLogger, INFO, StreamHandler, Formatter

import sys


INTERRUPT_EVENT = Event()


consumer = FlaskKafka(
    INTERRUPT_EVENT,
    bootstrap_servers=",".join(["localhost:9092"]),
    group_id="consumer-grp-id",
)

# setup logger for kafka consumer to log to stdout and format it
logger = getLogger("kafka_consumer")
logger.setLevel("DEBUG")
handler = StreamHandler(sys.stdout)
handler.setFormatter(Formatter('[%(asctime)s] [%(name)s] [%(levelname)s] [%(message)s]'))
logger.addHandler(handler)


@consumer.handle("reg-user")
def registration_user_topic_handler(msg: dict):
    logger.info(f"Received message: {msg}")
    try:
        data = loads(msg["value"].decode("utf-8"))
    except ValueError:
        logger.error(f"Failed to decode message: {msg}")
        return
    try:
        assert "username" in data
    except AssertionError:
        logger.error(f"Failed to validate data: {data}")
        return
    user = dbm.add_user(data)
    logger.info(f"User {user} was added to database")
