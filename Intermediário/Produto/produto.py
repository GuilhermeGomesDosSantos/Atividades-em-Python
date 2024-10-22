# 9 - Produto: Implemente uma classe Produto com atributos nome, preco e quantidade. Adicione métodos para calcular o valor total em estoque e atualizar o preço.

class Produto:
    def __init__(self, nome, preco, quantidade):
        self._nome = nome
        self._preco = preco
        self._quantidade = quantidade

    def __str__(self):
        return f"Produto: {self._nome}, Preço: R${self._preco}, Quantidade: {self._quantidade}"

    def atualizar_preco_produto(self, preco):
        self._preco = preco
        print(f"O produto {self._nome} seu preço foi atualizado para R${self._preco}")

    def calcular_preco_total_estoque(self):
        total = self._preco * self._quantidade

        print(f"O valor total em estoque do Produto {self._nome} é de R${total:.2f}")