# Empregado e Gerente: Crie uma classe Empregado e uma classe Gerente que herda de Empregado. Adicione métodos específicos para Gerente, como adicionar_funcionario.

from abc import ABC

class Empregado(ABC):
    def __init__(self, nome):
        self._nome = nome


