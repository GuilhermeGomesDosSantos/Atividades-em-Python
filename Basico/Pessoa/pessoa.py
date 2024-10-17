# Classe Pessoa: Crie uma classe Pessoa com atributos nome e idade. Adicione um método mostrar_informacoes que imprime o nome e a idade da pessoa.

class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    def mostrar_informacoes(self):
        print (f"O nome da pessoa é '{self._nome}' e a sua idade é '{self._idade}'")