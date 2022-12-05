from kafka.consumer.fetcher import ConsumerRecord
from flask_kafka import FlaskKafka
from threading import Event
from db_methods import dbm
from logging import getLogger, INFO, StreamHandler, Formatter

import sys
import os
import json


INTERRUPT_EVENT = Event()


consumer = FlaskKafka(
    INTERRUPT_EVENT,
    bootstrap_servers=",".join(["localhost:9092"]),
    group_id="1",
)

# setup logger for kafka consumer to log to stdout and format it
logger = getLogger("kafka_consumer")
logger.setLevel("DEBUG")
handler = StreamHandler(sys.stdout)
handler.setFormatter(Formatter('[%(asctime)s] [%(name)s] [%(levelname)s] [%(message)s]'))
logger.addHandler(handler)


@consumer.handle(os.getenv("PROFILE_TOPIC_NAME"))
def registration_user_topic_handler(msg: ConsumerRecord):
    logger.info(f"Received message: {msg}")
    data = json.loads(msg.value)
    username = data.get("name", None)
    if username is not None:
        data = {'username': username}
        user = dbm.add_user(data)
        logger.info(f"User {username} was added to database")
        return

    logger.error(f"Failed to get data: field name does not exist!")
