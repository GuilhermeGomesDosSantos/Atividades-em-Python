# Banco de Dados de Clientes: Crie uma classe BancoDeDados que armazena uma lista de clientes. Adicione métodos para adicionar, remover e buscar clientes.

class BancoDeDados:
    def __init__(self):
        self._lista_clientes = []

    def adicionar_cliente(self, nome_cliente):
        if nome_cliente != "":
            self._lista_clientes.append(nome_cliente)
            print(f"O cliente {nome_cliente} foi adicionado a lista com sucesso")
        else:
            print("Você não digitou de forma correta")
    
    def remover_cliente(self, nome_cliente):

        if nome_cliente != "":

            for nome in self._lista_clientes:
                print(f"{nome}")
                if nome_cliente == nome:
                    self._lista_clientes.remove(nome_cliente)
                    print(f"O cliente {nome_cliente} foi removido da lista")

                else:
                    print(f"O nome do cliente {nome_cliente} não foi encontrado na Base de dados")

    def buscar_cliente(self, nome_cliente):

        if nome_cliente != "":

            for nome in self._lista_clientes:

                if nome_cliente.lower() == nome.lower():
                    print(f"Cliente {nome_cliente} encontrado !!!")

                else:
                    print(f"O nome '{nome_cliente}' não pode ser encontrado na base de dados")

    def listar_clientes(self):
        if not self._lista_clientes:
            print("A lista está vazia!!!")

        print("Lista de clientes:")
        for i, nome in enumerate (self._lista_clientes, start = 1):
            print(f"{i} - Cliente: {nome}")