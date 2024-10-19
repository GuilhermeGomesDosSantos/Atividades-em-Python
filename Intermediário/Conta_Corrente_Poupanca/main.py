from Classes.ContaCorrente import ContaCorrente
from Classes.ContaPoupanca import ContaPoupanca

def main():

    # Criando uma Conta Poupança
    # conta_poupanca = ContaPoupanca("Guilherme", 2000, 67890)
    # conta_poupanca.rendimento_mensal()

    conta_corrente = ContaCorrente("Guilherme", 2000, 522141)
    conta_corrente.sacar(100)
if __name__ == "__main__":
    main()
