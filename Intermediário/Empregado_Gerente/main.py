from Gerente import Gerente

gerente_1 = Gerente("Guilherme")

def main():
    gerente_1.adicionar_funcionario("Fulano")
    gerente_1.adicionar_funcionario("Ciclano")
    gerente_1.adicionar_funcionario("ABCDEFG")
    gerente_1.listar_funcionarios()

if __name__ == "__main__":
    main()