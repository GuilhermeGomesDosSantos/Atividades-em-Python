from CarrinhoDeCompras import CarrinhoDeCompras

carrinho = CarrinhoDeCompras()

def main():
    carrinho.listar_produtos()
    carrinho.adicionar_produto()
    carrinho.listar_produtos()
    carrinho.remover_produtos()
    # carrinho.listar_produtos()
if __name__ == "__main__":
    main()