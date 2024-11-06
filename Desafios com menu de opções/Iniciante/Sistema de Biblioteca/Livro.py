# Biblioteca de Livros: Crie uma classe Livro com título, autor e ano de publicação. O menu deve permitir adicionar livros, listar e remover livros da biblioteca.

class Livro:
             
    def __init__(self):
        self.lista_de_livro = []

    def menu(self):
        print("""
        1 - Adicionar Livros
        2 - Listar Livros
        3 - Remover Livros
        """)

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            self.adicionar_livro()
            

    def adicionar_livro(self):

        while True:

            titulo = input("Titulo do livro: ")

            if not titulo:
                print("O livro não pode ser vazio")
                continue

            while True:
                autor = input(f"Qual o nome do autor do livro {titulo}? ")

                if not autor:
                    print(f"O titulo do livro {titulo} não pode ser vazio")
                    continue

                while True:
                    ano_publicacao = input(f"Qual foi o ano de publicação do livro {titulo}")

                    if not ano_publicacao:
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
            print("A lista de livros está vazia!!!")

        else:
            for book in self.lista_de_livro:
                print(f"Livro {book["Titulo"]}, Autor: {book["Autor"]}, ano de publicação: {book["Ano publicacao"]}")