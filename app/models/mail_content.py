from abc import ABC, abstractmethod

class MailContent(ABC):

    def __init__(self, from_mail:str, to_mail:str):
        self.data_mail = {}
        self.data_mail['from'] = f"Taco API <{from_mail}>"
        self.data_mail['to'] = to_mail

    def add_info(self, content):
        self.data_mail['subject'] = self.get_subject()
        self.data_mail['text'] = self.get_text(content)

    @abstractmethod
    def get_subject(self):
        pass

    @abstractmethod
    def get_text(self, content):
        pass

    def parse_dict(self) -> dict:
        return vars(self)['data_mail']    