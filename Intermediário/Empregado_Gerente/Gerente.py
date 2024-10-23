from Empregado import Empregado

class Gerente(Empregado):
    def __init__(self, nome):
        super().__init__(nome)
        self._lista_funcionarios = []

    def adicionar_funcionario(self, nome_funcionario):
        empregado = Empregado
        empregado = nome_funcionario
        self._lista_funcionarios.append(empregado)

        print(f"O Gerente {self._nome}, adicionou um novo funcionario\nFuncionario {empregado}")

    def listar_funcionarios(self):
        if not self._lista_funcionarios:
            print(f"A lista de funcionarios do Gerente {self._nome} está vazia!!!")

        print(f"Lista de Funcionarios do Gerente {self._nome}:")
        for i, empregado in enumerate(self._lista_funcionarios, start = 1):
            print(f'Funcionario {i} - {empregado}')
