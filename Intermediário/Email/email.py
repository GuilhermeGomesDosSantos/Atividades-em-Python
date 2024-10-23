# 15 - Conta de Email: Crie uma classe Email com atributos remetente, destinatario, assunto e mensagem. Adicione métodos para exibir e encaminhar o email.


class Email:
    def __init__(self, remetente, destinatario, assunto, mensagem):
        self._remetente = remetente
        self._destinatario = destinatario
        self._assunto = assunto
        self._mensagem = mensagem

    def exibir(self):
        print(f"Remetente: {self._remetente}")
        print(f"Destinatario: {self._destinatario}")
        print(f"Assunto: {self._assunto}")
        print(f"Mensagem: {self._mensagem}")

    def encaminhar_email(self, novo_remetente, novo_destinatario):
        print("Encaminhando o email...")
        print(f"Novo Remetente: {novo_remetente}")
        print(f"Novo Destinatario: {novo_destinatario}")
        print(f"Assunto: {self._assunto}")
        print(f"Mensagem: {self._mensagem}")