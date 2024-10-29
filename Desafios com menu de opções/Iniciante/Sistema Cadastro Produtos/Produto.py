# Sistema de Cadastro de Produtos: Crie uma classe Produto com atributos nome, preço e quantidade. Crie um menu para cadastrar, listar e remover produtos.

from os import system, name

class Produto:
    def __init__(self):
        self.produtos = {}

    def limpar_tela(self):
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')


    def listar_produto(self):
        self.limpar_tela()
        
        if not self.produtos:
            print("A lista de produtos está vazia!!!")

        else:
            print("Lista de Produtos:\n")
            for nome, info in self.produtos.items():
                print(f"Produto: {nome} - Valor R$ {info["preco"]:.2f}, quantidade: {info['quantidade']}")
            print("-" * 30)

        input("\nPressione 'Enter' para voltar ao menu")
    
    def menu_opcoes(self):

        while True:
            self.limpar_tela()

            print("""
            Escolha uma das opções abaixo:

            1 - Cadastrar Produto
            2 - Listar Produtos
            3 - Remover Produtos
            4 - Sair
            """)
            opcao = input("Digite uma opção: ").strip()

            if opcao == '1':
                self.cadastrar_produto()

            elif opcao == '2':
                self.listar_produto()

            elif opcao == '3':
                self.remover_produto()

            elif opcao == '4':
                self.limpar_tela()
                print('Finalizando Menu...')
                break

            else:
                print("Opção incorreta")
    
    def cadastrar_produto(self):
        while True:
            self.limpar_tela()
            produto = input("Digito o nome do produto: ")
            if not produto:
               print("Nome do produto está incorreto!!!")
               continue

            while True:
                preco = input(f"Informe o preço do Produto {produto} R$")
                if not preco.isnumeric():
                    print("Por favor digite apenas numeros")
                    continue
                else:
                    preco = float(preco)
                    break
            
            while True:
                quantidade = input(f"Informe a quantidade do Produto {produto}: ")
                if not quantidade.isnumeric():
                    print("Por favor digite apenas numeros")
                    continue
                else:
                    quantidade = int(quantidade)
                    break

            
            self.produtos[produto] = {"preco": preco, "quantidade": quantidade}

            print("Produto cadastrado")
            print(f"Produto: {produto} - Preço: R${preco} - Quantidade: {quantidade}")

            continuar = input("Você deseja adicionar outro produto? [s / n] ").strip().lower()

            if continuar in ("n", "não"):
                break
    
    def remover_produto(self):
        self.limpar_tela()

        if not self.produtos:
            print("a lista de produtos está vazia!!!")
            input("Pressione 'Enter' para voltar ao menu")
            return
        
        while True:
            produto_remover = input("Qual produto você quer remover ?")

            if produto_remover in self.produtos:
                del self.produtos[produto_remover]
                print(f"O produto {produto_remover} foi removido da lista")

            elif not self.produtos:
                print("A lista de produtos está vazia")
                input("Digite 'enter' para sair")
                break
            
            else:
                print(f"O produto {produto_remover} não existe na lista")
            
            continuar = input("Deseja apagar outro produto ? [s / n] ").strip().lower()
            if continuar in ("n", "não"):
                break