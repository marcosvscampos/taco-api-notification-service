from app.services.mail.api_key_mail_service import ApiKeyMailService

def get_instance(type:str):
    instances = [
        { "API_KEY_CREATED":  ApiKeyMailService() }
    ]

    for item in instances:
        return item[type]