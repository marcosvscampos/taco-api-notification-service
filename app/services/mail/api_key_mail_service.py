from app.services.mail.mail_service import MailService
from app.models.api_key_mail_content import ApiKeyMailContent

class ApiKeyMailService(MailService):

    def __init__(self):
        super().__init__()

    def _build_mail(self, to:str, content) -> dict:
        mail_content = ApiKeyMailContent(
                from_mail=self.config.from_mail,
                to_mail=to)
        mail_content.add_info(content)
        return mail_content.parse_dict()