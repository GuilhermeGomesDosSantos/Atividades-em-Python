from Banco import Banco

banco_1 = Banco()
banco_2 = Banco()
banco = Banco()

def main():
    banco.criar_conta("Guilherme",123, 1000)
    banco.criar_conta("Fulano",321, 1500)
    banco.transferir_dinheiro(123,321, 999)
    banco.exibir_saldo()

if __name__ == "__main__":
    main()