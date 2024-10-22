# 8 - Biblioteca: Crie uma classe Biblioteca que gerencia uma coleção de livros. Adicione métodos para adicionar livros, emprestar livros e retornar livros.

from livro import Livro


class Biblioteca:
    def __init__(self):
        self._livros = []

    def listar_livros(self):
        if not self._livros:
            print("Não há livros na biblioteca!!!")

        else:
            print("Listando livros da biblioteca!!!")
            print(
                f'{"Livro".ljust(25)} | {"Autor".ljust(25)} | {"Ano".ljust(25)} | {"Livro disponivel ? :"}'
            )

        for livro in self._livros:
            disponivel = (
                f"Livro está disponivel" if livro._status else "Livro indisponivel"
            )
            print(
                f"{livro._titulo.ljust(25)} | {livro._autor.ljust(25)} | {str(livro._ano).ljust(25)} | {disponivel.ljust(25)}"
            )

    def adicionar_livro(self, livro):
        self._livros.append(livro)
        print(f"O livro {livro._titulo}, foi adicionado a biblioteca")

    def emprestar_livro(self, titulo):
        for livro in self._livros:
            if livro._titulo == titulo:
                if livro._status:
                    livro._status = False
                    print(f"O livro {livro._titulo} foi emprestado com sucesso")
                    return
                else:
                    print(f"O livro {livro._titulo} ja foi emprestado!!!")
                    return

            print(f"O livro {livro._titulo} não foi encontrado")

    def devolver_livro(self, titulo):
        for livro in self._livros:
            if livro._titulo == titulo and livro._status == False:
                livro._status = True
                print(f"O livro {livro._titulo}, foi devolvido")

            elif livro._titulo == titulo and livro._status == True:
                print(f"O livro {livro._titulo} ainda não foi emprestado")
        else:
            print(f"O livro {titulo} não existe na base de dados da biblioteca")
