from .ContaBancaria import ContaBancaria

class ContaCorrente(ContaBancaria):
    def __init__(self, titular, saldo, n_conta):
        super().__init__(titular, saldo, n_conta)
    
    def sacar(self, valor):
        valor
        if valor > self._saldo:
            print(f"Saldo: R${self._saldo}")
            print(f"Saque de {self._saldo}, não pode ser realizado, pois é maior do que o seu saldo!!!")
        
        elif valor > 0 and valor < self._saldo:
            novo_valor = self._saldo - valor

            print(f"Saldo R$: {self._saldo}")
            print(f"Transferencia realizada com sucesso")
            print(f"Saldo apos transação: R${novo_valor}")

        else:
            print("Error")