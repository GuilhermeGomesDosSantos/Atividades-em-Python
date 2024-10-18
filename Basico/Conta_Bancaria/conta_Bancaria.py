# 3 - Conta Bancária: Implemente uma classe ContaBancaria com métodos para depositar e sacar dinheiro, além de um método para mostrar o saldo atual.

class Conta_Bancaria:
    def __init__(self):
        self._saldo = 1000

    def sacar(self):
        print(f"Saldo atual R$ {self._saldo:.2f}")

        while True:

            try:
                valor_sacar = float(input('Informe qual valor você deseja sacar R$: '))
                
            
                if self._saldo < valor_sacar:
                    print(f"Transação não efetuada, seu saldo é menor do que o valor de R$ {valor_sacar:.2f} solicitado para transação")
                elif self._saldo >= valor_sacar:
                    self._saldo -= valor_sacar
                    print(f'Transferencia realizada com sucesso!!!')
                    break
                # else:
                     
            except ValueError:
                    print("Valor incorreto!!!")

    def depositar(self):
        print(f"Saldo atual R${self._saldo:.2f}")
        
        valor_depositar = float(input('Informe qual é o valor que você deseja depositar R$ '))
        
        self._saldo += valor_depositar
        print(f"Deposito realizado com sucesso\nSeu saldo é de agora R$ {self._saldo:.2f}")

    def mostrar_saldo(self):
        print(f"Seu saldo atual é de R$ {self._saldo:.2f}")