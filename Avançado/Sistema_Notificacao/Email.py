class Email:
    def __init__(self, nome_remetente, e_mail_remetente, nome_destinatario, e_mail_destinatario, assunto, menssagem):
        self._nome_remetente = nome_remetente
        self._e_mail_remetente = e_mail_remetente
        self._nome_destinatario = nome_destinatario
        self._email_destinatario = e_mail_destinatario
        self._assunto = assunto
        self._mensagem = menssagem