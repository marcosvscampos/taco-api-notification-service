from app.config.amqp import AMQPProvider
from dotenv import load_dotenv
from app.utils import banner

load_dotenv()

def run():
    banner()
    provider = AMQPProvider()
    print(f">>> Waiting for messages...")
    run_consumer = True
    while(run_consumer):

        try:
            provider.channel.start_consuming()
        except Exception as e:
            print(e)
            provider.channel.stop_consuming()
            run_consumer = False
            provider.close_connection()    
    
if (__name__ == '__main__'):
    run()