# 19 - Veículo e Transporte: Crie uma hierarquia de classes onde Veiculo é a classe base e Carro, Moto e Caminhao herdam dela. Cada tipo de veículo deve ter métodos específicos.

from abc import ABC

class Veiculo(ABC):

    def __init__(self, marca):
        self._marca = marca
