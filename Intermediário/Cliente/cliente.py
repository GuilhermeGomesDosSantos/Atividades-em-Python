# 10 - Cliente: Crie uma classe Cliente que tenha atributos nome e lista_compras (uma lista de produtos).
# Adicione métodos para adicionar um produto à lista e calcular o total da lista.


class Cliente:
    def __init__(self, nome):
        self._nome = nome
        self._lista_produtos = []

    def adicionar_produto(self, produto, preco):
        self._lista_produtos.append((produto, preco))

        print (f"O cliente: {self._nome} adicionou o produto {produto} no valor de R${preco:.2f} a sua lista de produtos")
    
    def mostrar_lista(self):
        if not self._lista_produtos:
            print(f"A lista do cliente {self._nome} está vazia")
    
        print("Lista de Produtos!!!")
        print(f'{"Produto".ljust(20)} | {"Preço R$".ljust(20)}')

        for produto, preco in self._lista_produtos:
            print(f'{produto.ljust(20)} | {preco:.2f}')

    def valor_total_lista(self):
        if not self._lista_produtos:
            print(f"A lista do cliente {self._nome} está vazia")

        total = 0
        for produto, preco in self._lista_produtos:
            total += preco
        print(f"O valor total da lista de produtos do cliente {self._nome} é de {total:.2f}")