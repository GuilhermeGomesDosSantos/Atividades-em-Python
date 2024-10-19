from funcionario import Funcionario

funcionario_1 = Funcionario("Guilherme", 1999, "Desenvolvedor de APIs")

def main():
    funcionario_1.info_funcionario()
    funcionario_1.aumentar_salario()

if __name__ == "__main__":
    main()