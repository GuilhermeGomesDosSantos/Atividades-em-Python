from livro import Livro
from biblioteca import Biblioteca

livro_1 = Livro("Abc", "Guilherme", 2222)
livro_2 = Livro("AAABBB", "GDS", 2022)
livro_3 = Livro("ABCDE", "Gui", 2010)
biblioteca_1 = Biblioteca()
def main():
    # print(livro_1)
    biblioteca_1.adicionar_livro(livro_1)
    biblioteca_1.adicionar_livro(livro_2)
    biblioteca_1.adicionar_livro(livro_3)
    biblioteca_1.listar_livros()
    biblioteca_1.emprestar_livro("Abc")
    biblioteca_1.devolver_livro("AAA")
if __name__ == "__main__":
    main()