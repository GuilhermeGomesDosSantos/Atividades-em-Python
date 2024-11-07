# Biblioteca de Livros: Crie uma classe Livro com título, autor e ano de publicação. O menu deve permitir adicionar livros, listar e remover livros da biblioteca.

from os import system, name

class Livro:
             
    def __init__(self):
        self.lista_de_livro = []

    def limpar_tela(self):
        if name == "nt":
            _ = system("cls")
        else:
            _ = system("clear")

    def menu(self):
        self.limpar_tela()

        while True:
            print("""
            1 - Adicionar Livros
            2 - Listar Livros
            3 - Remover Livros
            4 - Sair
            """)

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.limpar_tela()
                self.adicionar_livro()

            elif opcao == "2":
                self.limpar_tela()
                self.listar_livros()

            elif opcao == "4":
                self.limpar_tela()
                print("Saindo...")
                break

    def adicionar_livro(self):

        while True:

            titulo = input("Titulo do livro: ")

            if not titulo:
                self.limpar_tela()
                print("O livro não pode ser vazio")
                continue

            while True:
                self.limpar_tela()
                autor = input(f"Qual o nome do autor do livro {titulo}? ")

                if not autor:
                    self.limpar_tela()
                    print(f"O titulo do livro {titulo} não pode ser vazio")
                    continue

                while True:
                    self.limpar_tela()
                    ano_publicacao = input(f"Qual foi o ano de publicação do livro {titulo}")

                    if not ano_publicacao:
                        self.limpar_tela()
                        print(f"A data de publicação do livro {titulo} não pode ser vazia")
                        continue
                    break
                break

            self.lista_de_livro.append({
                "Titulo": titulo,
                "Autor": autor,
                "Ano publicacao": int(ano_publicacao)
            })

            while True:
                self.limpar_tela()
                continuar = input("Deseja adicionar outro livro? s / n -> ").strip().lower()
                
                if continuar in ["s", "n", "sim", "não"]:
                    break

                else:
                    print("Por favor digite uma das opções")
                    print("S -> sim para continuar")
                    print("N -> para sair")
                    continue

            if continuar == "n" or continuar == "não":
                break

    def listar_livros(self):
        if not self.lista_de_livro:
            input("A lista de livros está vazia!!!\Pressione 'Enter' para voltar")
            self.limpar_tela()
        
        else:
            for book in self.lista_de_livro:
                print(f"Livro {book["Titulo"]}, Autor: {book["Autor"]}, ano de publicação: {book["Ano publicacao"]}")

            
            input("Pressione 'Enter' para voltar")
            self.limpar_tela()