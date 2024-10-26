# 23 - Jogo de Cartas: Implemente uma classe Carta com atributos valor e naipe. Crie uma classe Baralho que gerencia uma lista de cartas e tem métodos para embaralhar e distribuir cartas.

class Carta:
    def __init__(self, valor, naipe):
        self._valor = valor
        self._naipe = naipe

    def __str__(self):
        return f"{self._valor} de {self._naipe}"