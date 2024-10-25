from Funcionario import Funcionario
from FuncionarioComissionado import FuncionarioComissionado

funcionario_1 = Funcionario("Guilherme", 2000)
funcionario_comissao = FuncionarioComissionado("Guilherme Comissão", 2000)

def main():
    funcionario_1.calcular_salario_por_hr(8)
    funcionario_comissao.calcular_comissao(1000)

if __name__ == "__main__":
    main()