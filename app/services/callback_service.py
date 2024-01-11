from app.services.mail import mail_strategy
from app.services.mail.mail_service import MailService
from app.exceptions.mail_integration_exception import MailIntegrationException
import json

def notification_msg_callback(ch, method, properties, body):
        try:
                json_body = json.loads(body)
                mail_service:MailService = mail_strategy.get_instance(json_body['type'])
                mail_service.send(json_body["content"])
                print(f"[amqp_service#notification_msg_callback] >>> Email successful sent to {json_body['content']['email']}!")
                ch.basic_ack(delivery_tag=method.delivery_tag)
        
        except MailIntegrationException as mie:
                print(f">>> ERROR: {mie} \n - Cause: {mie.cause}")       