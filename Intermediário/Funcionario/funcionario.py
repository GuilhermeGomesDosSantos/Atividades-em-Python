# 6 - Funcionário: Implemente uma classe Funcionario com atributos nome, salario e cargo. Adicione métodos para aumentar o salário e exibir informações do funcionário.

class Funcionario:
    def __init__(self, nome, salario: 2000, cargo):
        self._nome = nome
        self._salario = salario
        self._cargo = cargo

    def aumentar_salario(self):


        while True:

            try:
                valor = float(input(f"Digite o novo valor que o funcionario '{self._nome} irá receber: R$'"))
                
                if valor > 0:
                    self._salario = valor

                    print(f"Salario atualizado com sucesso, o novo valor é de R${self._salario}")
                    break
                else:
                    print(f"O valor precisa ser maior que 0 (Zero), digite novamente porfavor!")
                
            except ValueError:
                print("ERRO!!!, valor fornecido está incorreto, digite o valor correto porfavor!")

    def info_funcionario(self):
        print(f"Informações do Funcionario '{self._nome}'\nNome: {self._nome}\nCargo: {self._cargo}\nSalario: R${self._salario:.2f}")