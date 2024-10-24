from Iventario import Iventario

estoque = Iventario()

def main():
    estoque.adicionar("Arroz", 5)
    estoque.listar_itens()
    estoque.remover("Arroz")
    estoque.listar_itens()
    estoque.adicionar("Arroz", 5)
    estoque.listar_itens()

    estoque.adicionar_quantidade_item("Arroz", 10)

if __name__ == "__main__":
    main()