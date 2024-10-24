from Cliente import BancoDeDados

cliente = BancoDeDados()

def main():
    cliente.adicionar_cliente("Guilherme")
    cliente.adicionar_cliente("Fulano")
    cliente.adicionar_cliente("Ciclano")
    # cliente.remover_cliente("Guilherme")
    # cliente.buscar_cliente("Guilherme")
    cliente.listar_clientes()

if __name__ == "__main__":
    main()