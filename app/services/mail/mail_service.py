import requests

from app.config.environment.mail_env_config import MailEnvConfig
from app.exceptions.mail_integration_exception import MailIntegrationException
from abc import ABC, abstractmethod

class MailService(ABC):
    
    def __init__(self):
        self.config = MailEnvConfig()

    def send(self, to:str, content:dict):
        try: 
            requests.post(
                url=self.config.api_full_url,
                auth=("api", self.config.api_key),
                data=self._build_mail(to, content))
        except requests.ConnectionError as ce:
            raise MailIntegrationException(ce)
        except requests.HTTPError as he:
            raise MailIntegrationException(he)
            
    @abstractmethod    
    def _build_mail(self, to:str, content:dict) -> dict:
        pass    