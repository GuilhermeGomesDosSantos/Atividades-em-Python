# 13 - Circulo: Implemente uma classe Circulo com atributo raio. Adicione métodos para calcular a área e a circunferência do círculo.

class Circulo:
    def __init__(self, raio):
        self._raio = raio
        self.pi = 3.14

    def calcular_area(self):
        area = self.pi * (self._raio * self._raio)
        print(f"O valor da Area é: {area:.2f}")

    def calcular_circulo(self):
        circuferencia = 2 * self.pi * self._raio
        print(f"O valor da circuferencia é: {circuferencia:.2f}")

