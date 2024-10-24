from Veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, marca):
        super().__init__(marca)

    def acionar_pedaleira(self):
        print(f"A Moto {self._marca} está abaixando a pedaleira para o passageiro")