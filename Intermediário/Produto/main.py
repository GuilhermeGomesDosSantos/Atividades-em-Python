from produto import Produto

produto_1 = Produto("Carne", 20, 5)

def main():
    produto_1.atualizar_preco_produto(100)
    produto_1.calcular_preco_total_estoque()

if __name__ == "__main__":
    main()