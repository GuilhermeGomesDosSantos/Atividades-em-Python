class Livro:
    def __init__(self, titulo, autor, ano):
        self._titulo = titulo
        self._autor = autor
        self._ano = ano
        self._status = True

    def __str__(self):
        return f"Livro: {self._titulo}, autor: {self._autor}, ano: {self._ano}, Livro disponivel? : {self._status}"
    
    