# 24 - Sistema de Login: Crie uma classe Usuario com atributos nome, senha e email. Adicione métodos para autenticação e alteração de senha.

class Usuario:
    def __init__(self, nome, senha, email):
        self._nome = nome
        self._senha = senha
        self._email = email

    def autenticacao(self, email_user, senha_user):
        if not email_user and not senha_user:
            print('Você não forneceu a senha e e-mail!!!')
        elif email_user != self._email and senha_user != self._senha:
            print('Os dados estão incorretos')
        elif not email_user:
            print('Você não fornceu o E-mail!!!')
        elif not senha_user:
            print('Você não fornceu senha!!!')
        elif email_user != self._email:
            print("Esse e-mail não existe em nossa base")
        else:
            print(f"Olá {self._nome}, login realizado pelo E-mail: {email_user} completo")

    def atualizar_senha(self, nova_senha):
        if nova_senha == "":
            print("A senha não pode ser vazia!!!")
        else:
            self._senha == nova_senha
            print("Senha atualizada com sucesso!!!")