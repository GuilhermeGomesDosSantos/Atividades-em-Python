from Carta import Carta

import random

class Baralho:
    def __init__(self):
        valores = ["Ás", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Valete", "Dama", "Rei"]
        naipes = ["Copas", "Espadas", "Ouros", "Paus"]
        self.cartas = []

        for valor in valores:
            for naipe in naipes:
                carta = Carta(valor, naipe)
                self.cartas.append(carta)

    def embaralhar(self):
        random.shuffle(self.cartas)

    def distribuir(self, qtd_cartas):
        if qtd_cartas > len(self.cartas):
            print(f"A quantidade de cartas solicitada é maior do que a do baralho")
            return []
        
        cartas_distribuidas = []
        for _ in range(qtd_cartas):
            carta = self.cartas.pop()
            cartas_distribuidas.append(carta)

        return cartas_distribuidas