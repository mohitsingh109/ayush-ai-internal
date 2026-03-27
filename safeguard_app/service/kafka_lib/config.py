class KafkaConfig:

    def __init__(
            self,
            bootstrap_servers: str,
            topic: str,
            auto_offset_reset: str = 'earliest',
            group_id: str = None,
            retries: int = 3,
            acks: str = 'all'
    ):
        self.bootstrap_1 = bootstrap_servers
        self.topic = topic
        self.auto_offset_reset = auto_offset_reset
        self.group_id = group_id
        self.retries = retries
        self.acks = acks
