# 27 - Sistema de Compras: Implemente uma classe CarrinhoDeCompras que armazena produtos e calcula o total da compra. Adicione métodos para adicionar e remover produtos.

class CarrinhoDeCompras:
    def __init__(self):
        self.lista_produtos = {}

    def adicionar_produto(self):
        while True:
            produto = input("Nome do Produto: ").strip()

            if not produto:
                print("Nome do produto está vazio, preencha novamente!!!")
                continue
            
            while True:
                valor_produto = input(f"Informe o valor do Produto '{produto}' R$: ")

                if not valor_produto:
                    print(f"O valor do Produto '{produto}' não foi adicionado da forma correta")
                    continue

                elif valor_produto.isnumeric():
                    self.lista_produtos[produto] = valor_produto
                    break

                else:
                    print("O valor informado não é numerico")

            while True:
                continuar = input("Deseja continuar adicionando outro Produto? [s / n]: ").strip().lower()

                if continuar == "n" or continuar == "não":
                    break
                
                elif continuar == "s" or continuar == "sim":
                    break

                else:
                    print("Por favor digite uma das opções: 's' para continuar ou 'n' para sair.")

            print(f"Produto: {produto} - Valor: R$: {valor_produto} foi registrado")
            if continuar == "n" or continuar == "não":
                break


    def listar_produtos(self):
        if not self.lista_produtos:
            print("A lista de produtos está vazia !!!")

        else:
            print("Lista de Produtos:")
            for produto, valor in self.lista_produtos.items():
                print(f"Produto: {produto} - R$: {valor}")

    def remover_produtos(self):

        while True:
            item_remover = input("Informe o nome do produto que deseja remover: ").strip()

            if item_remover in self.lista_produtos:
                self.lista_produtos.pop(item_remover)
                print(f"O item {item_remover} foi removido")

            elif not item_remover or item_remover == "":
                print("Por favor insira o nome do Produto!!!")
                continue

            else:
                print(f"O item {item_remover}, não foi encontrado")
                continue

            while True:

                if len(self.lista_produtos) == 0:
                    continuar = "n"
                    print("A lista de produtos está vazia")
                    print("Encerrando processo !!!")
                    break
            
                continuar = input("Deseja remover outro produto ? [s / n] ").strip().lower()

                if continuar == "n" or continuar == "não":
                    break

                elif continuar == "s" or continuar == "sim":
                    break

                else:
                    print("Por favor digite uma das opções: 's' para continuar ou 'n' para sair.")

            if continuar == "n" or continuar == "não":
                break