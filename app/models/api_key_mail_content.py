from app.models.mail_content import MailContent

class ApiKeyMailContent(MailContent):

    def __init__(self, from_mail:str, to_mail:str):
        super().__init__(
            from_mail=from_mail,
            to_mail=to_mail
        )

    def get_subject(self):
        return 'Bem-Vindo! Receba sua chave de acesso'

    def get_text(self, content):
        user_key = content['key']
        return f'Olá! Aqui está a sua chave de acesso para começar a usar a TACO API: {user_key}'    

