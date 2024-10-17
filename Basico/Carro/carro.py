# 2 - Classe Carro: Crie uma classe Carro com atributos marca, modelo e ano. Adicione um método exibir_detalhes que imprime as informações do carro.

class Carro:
    def __init__(self, marca, modelo, ano):
        self._marca = marca
        self._modelo = modelo
        self._ano = ano

    def exibir_detalhes(self):
        print(f'Informações do Carro!!!\nMarca: {self._marca}, Modelo: {self._modelo}, Ano: {self._ano}')