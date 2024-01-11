import os
from app.config.environment.env_config import EnvConfig

class AMQPEnvConfig(EnvConfig):

    def __init__(self):
        self.host = os.environ.get("AMQP_HOST")
        self.username = os.environ.get("AMQP_USERNAME")
        self.password = os.environ.get("AMQP_PASSWORD")
        self.vhost = os.environ.get("AMQP_VHOST")
        self.queue_name = os.environ.get("AMQP_QUEUE_NAME")
        super().__init__()
    
    def print_info(self):
        print(f">>> Connected into: Queue - {self.queue_name} | Host - {self.host} | VHost - {self.vhost}")