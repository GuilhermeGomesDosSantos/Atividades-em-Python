from cliente import Cliente

cliente_1 = Cliente("Guilherme")

def main():
    cliente_1.adicionar_produto("Prod 1", 20)
    cliente_1.adicionar_produto("Prod 1", 211)
    cliente_1.mostrar_lista()
    # cliente_1.valor_total_lista()

if __name__ == "__main__":
    main()