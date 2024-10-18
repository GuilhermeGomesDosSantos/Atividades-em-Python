# 4 - Retângulo: Crie uma classe Retangulo com atributos largura e altura. Adicione métodos para calcular a área e o perímetro do retângulo.

class Retangulo:
    def __init__(self, largura = 0, altura = 0):
        self._largura = largura
        self._altura = altura

    def calcular_area(self):
        valor_largura = (float(input('Informe o valor da largura: ')))
        valor_altura = (float(input('Informe o valor da altura: ')))

        area = valor_largura * valor_altura
        print(f'O valor da Area do triangulo é: {area}')

    def calcular_perimetro(self):
        valor_largura = (float(input('Informe o valor da largura: ')))
        valor_altura = (float(input('Informe o valor da altura: ')))

        perimetro = 2 * (valor_largura + valor_altura)
        print(f'O valor do perimetro é: {perimetro}')