# 20 - Sistema de Inventário: Implemente uma classe Inventario para gerenciar itens em um estoque. Adicione métodos para adicionar, remover e listar itens.


class Iventario:
    def __init__(self):
        self.dicionario_item = {}

    def listar_itens(self):
        if not self.dicionario_item:

            print("A lista está vazia")

        for produto, quantidade in self.dicionario_item.items():
            print(f"Item: {produto} - Quantidade: {quantidade}")

    def adicionar(self, item, quantidade):
        # Quando você faz essa atribuição, o Python está dizendo: "No dicionário dicionario_item, a chave item deve ter o valor quantidade"
        self.dicionario_item[item] = quantidade

        print(f"{quantidade} unidade(s) de {item} foram adicionados ao iventario")

    def remover(self, item):
        if item in self.dicionario_item:
            self.dicionario_item.pop(item)
            print(f"O item {item}, foi removido")

    def adicionar_quantidade_item(self, item, quantidade):

        if item in self.dicionario_item:
            self.dicionario_item[item] += quantidade  # Atualiza a quantidade somando
            print(f"O item {item} sua quantidade foi atualizada para: {self.dicionario_item[item]}")
        else:
            print(f"O item {item} não foi encontrado.")