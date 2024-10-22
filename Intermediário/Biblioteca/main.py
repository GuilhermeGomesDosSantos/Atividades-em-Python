from livro import Livro
from biblioteca import Biblioteca

livro_1 = Livro("Abc", "Guilherme", 2222)
biblioteca_1 = Biblioteca()
def main():
    print(livro_1)
    biblioteca_1.adicionar_livro(livro_1)

if __name__ == "__main__":
    main()