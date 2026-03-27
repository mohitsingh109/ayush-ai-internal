from safeguard_app.service.kafka_lib.producer.producer import BaseProducer


class KafkaProducerService:
    def __init__(self, base_producer: BaseProducer):
        self.producer = base_producer.producer

    def send_message(self, topic: str, msg: dict, key: str = None):
        pass

