# TACO API NOTIFICATION SERVICE

### Descrição

Esse projeto é um Microserviço criado para receber eventos de outros serviços e enviar notificações via email. 
Atualmente ele tem o objetivo de enviar a API-KEY para o usuário cadastrado via email.

## Tecnologias

* MailGun
* Requests
* RabbitMQ (pika)
* Python 3.12

## Observações

Antes de iniciar, você deve criar um arquivo .env na raiz do projeto para estabelecer os valores de banco de dados e messageria.

| Variável | Descrição |
| -------- | ------- |
| AMQP_HOST | Host de conexão com o RabbitMQ |
| AMQP_VHOST | Nome do vhost da conexão do RabbitMQ |
| AMQP_USERNAME | Nome do usuário de conexão com o RabbitMQ |
| AMQP_PASSWORD | Senha de conexão do RabbitMQ |
| AMQP_QUEUE_NAME | Nome da fila onde as notificações são enviadas |
| MAIL_DOMAIN | Nome do dominio do serviço de email |
| MAIL_API_KEY | Chave da API para autenticação no serviço de email |
| MAIL_API_URL | URL de conexão com a API de email |
| MAIL_FROM_PREFIX | Prefixo do email do remetente |
| APP_VERSION | Versão atual da aplicação |

## Pontos importantes

Como citado anteriormente, o serviço de email escolhido foi o MailGun.
Portanto as variáveis do tipo MAIL são as informações providenciadas pela própria MailGun.
Sugiro que você faça seu cadastro em https://www.mailgun.com/ para conseguir realizar as configurações do provedor de email.

OBS: Foi usado o RabbitMQ Cloud para realizar o desenvolvimento desse projeto

## Endpoints

v.0.0.1  
* GET - /api/users/{user_id} - Retorna um usuário dado seu ID
* POST - /api/users - Cadastra um novo usuário


