from Funcionario import Funcionario

class FuncionarioComissionado(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)

    def calcular_comissao(self, valor_venda):
        comissao = valor_venda * 0.1 # o funcionario irá receber 10% de comissão
        print(f"O funcionario {self._nome}, vendeu R${valor_venda:.2f}, o total de comissão é de R${comissao:.2f}")