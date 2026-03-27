from kafka import KafkaProducer

from safeguard_app.service.kafka_lib.config import KafkaConfig


class BaseProducer:

    def __init__(self, config: KafkaConfig):
        self.producer = KafkaProducer(bootstrap_servers = config.bootstrap_1,retries = config.retries,acks = config.acks)