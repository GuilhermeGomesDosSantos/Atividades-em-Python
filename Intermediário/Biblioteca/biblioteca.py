# 8 - Biblioteca: Crie uma classe Biblioteca que gerencia uma coleção de livros. Adicione métodos para adicionar livros, emprestar livros e retornar livros.

from livro import Livro

class Biblioteca:
    def __init__(self):
        self._livros = []

    def adicionar_livro(self, livro):
        self._livros.append(livro)
        print(f"O livro {livro._titulo}, foi adicionado a biblioteca")

    # def emprestar_livro(self, livro):
