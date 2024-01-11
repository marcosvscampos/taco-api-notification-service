import pika
from app.config.environment.amqp_env_confg import AMQPEnvConfig
from app.services.callback_service import notification_msg_callback

class AMQPProvider:

    def __init__(self):
        config = AMQPEnvConfig()
        url: str = f'amqps://{config.username}:{config.password}@{config.host}/{config.vhost}'
        parameters = pika.URLParameters(url)
        self.__connection = pika.BlockingConnection(parameters)
        self.__channel = self.__connection.channel()
        self.__init_consumer(config)

    def __init_consumer(self, config:AMQPEnvConfig):
        self.__channel.basic_consume(queue=config.queue_name, on_message_callback=notification_msg_callback, auto_ack=False)

    def close_connection(self):
        self.__connection.close()

    @property
    def channel(self):
        return self.__channel        