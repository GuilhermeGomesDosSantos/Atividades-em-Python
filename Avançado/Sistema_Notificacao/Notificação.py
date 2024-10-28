# 29 - Sistema de Notificações: Implemente uma classe Notificacao com métodos para enviar notificações por e-mail, SMS e push. Adicione subclasses específicas para cada tipo de notificação.

from Email import Email
from SMS import SMS
from Push import Push

email_1 = Email("Guilherme Gomes", "teste@gmail.com", "Destinatario 123", "destinatario@gmail.com", "Desafio 29", "Fazendo desafio 29")
sms_1 = SMS(123456789, "Guilherme Gomes", 987654321, "Fulano teste", "Fazendo desafio 29")
push_1 = Push(123321, "Desafio 29", "Fazendo desafio 29")
class Notificacao:
    def __init__(self):
        pass

    def enviar_email(self):
        print(f"Nome remetente: {email_1._nome_remetente} - Email: {email_1._e_mail_remetente}\n" + f"Nome destinatario: {email_1._nome_destinatario} - Email - {email_1._email_destinatario}\n" + f"Assunto: {email_1._assunto}\nMensagem: {email_1._mensagem}")

    def enviar_sms(self):
        print(f"N° do remetente: {sms_1._n_remetente} - Nome: {sms_1._nome_remetente}\n" + f"N° do destinatario: {sms_1._n_destinatario} - Nome: {sms_1._nome_destinatario}\n" + f"Assunto: {sms_1._assunto}")

    def enviar_push(self):
        print(f"ID do destinatario: {push_1._destinatario_id}\n" + f"Titulo {push_1._titulo}\n" + f"Mensagem: {push_1._mensagem}")