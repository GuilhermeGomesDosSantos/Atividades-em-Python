# 21 - Funcionário e Pagamento: Crie uma classe Funcionario com um método para calcular o salário baseado em horas trabalhadas. Implemente uma classe FuncionarioComissionado que herda de Funcionario e calcula comissões.


class Funcionario:
    def __init__(self, nome, salario):
        self._nome = nome
        self._salario = salario

    def calcular_salario_por_hr(self, hr):
        salario_dia = self._salario / 30
        salario_hr = salario_dia / hr

        print(f"O salario do Funcionario {self._nome} por {hr} horas tranalhadas é de R${salario_hr:.2f}")