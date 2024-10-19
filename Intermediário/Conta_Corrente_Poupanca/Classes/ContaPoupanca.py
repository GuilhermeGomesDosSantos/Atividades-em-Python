from .ContaBancaria import ContaBancaria

class ContaPoupanca(ContaBancaria):
    def __init__(self, titular, saldo, n_conta):
        super().__init__(titular, saldo, n_conta)
    
    def rendimento_mensal(self):
            rendimento = self._saldo * 0.02  # 2% de rendimento ao mês
            self._saldo += rendimento
            print(f"Rendimento de R${rendimento} adicionado ao saldo de {self._titular}. Saldo atual: R${self._saldo}")