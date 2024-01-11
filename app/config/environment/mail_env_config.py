from app.config.environment.env_config import EnvConfig
import os

class MailEnvConfig(EnvConfig):

    def __init__(self):
        mail_prefix = os.environ.get("MAIL_FROM_PREFIX")
        api_url = os.environ.get("MAIL_API_URL")
        self.domain = os.environ.get("MAIL_DOMAIN")
        self.api_key = os.environ.get("MAIL_API_KEY")
        self.from_mail = f"{mail_prefix}@{self.domain}"
        self.api_full_url = f"{api_url}/{self.domain}/messages"
        super().__init__()

    def print_info(self):
        print(f">>> Mail Server connected into: URL - {self.api_full_url} | Domain - {self.domain} | From Addr - {self.from_mail}")    
        