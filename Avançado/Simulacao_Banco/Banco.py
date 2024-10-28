# Simulação de Banco: Crie uma classe Banco com métodos para criar contas, transferir dinheiro entre contas e exibir o saldo de todas as contas.

class Banco:
    def __init__(self):
        self.contas = {}

    def criar_conta(self, nome_user, numero_conta, saldo_inicial = 0):
        self.contas[numero_conta] = saldo_inicial
        print(f"Conta nova criada, Usuário '{nome_user}', N°: {numero_conta} - Saldo de R${saldo_inicial}")

    def transferir_dinheiro(self, conta_remetente, conta_destino, valor):
        if conta_remetente not in self.contas:
            print(f"A conta remetente {conta_remetente}, não existe na base do banco")
            return

        elif conta_destino not in self.contas:
            print(f"A conta destino {conta_destino}, não existe na base do banco")
            return

        if self.contas[conta_remetente] <= valor:
            print(f"Saldo insuficiente para essa transação")
            return
        
        self.contas[conta_remetente] -= valor
        self.contas[conta_destino] += valor

        print(f"Transferia de {valor} realizada pela conta {conta_remetente} para a conta de destino {conta_destino} no valor de {valor} foi concluida com sucesso")

    def exibir_saldo(self):
        if not self.contas:
            print("Não há nenhuma conta criada até o momento")
        for conta, saldo in self.contas.items():
            print(f"N° da conta: {conta} - Saldo de R${saldo:.2f}")