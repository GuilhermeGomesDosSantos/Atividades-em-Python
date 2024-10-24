from Veiculo import Veiculo

class Caminhao(Veiculo):
    def __init__(self, marca):
        super().__init__(marca)

    def descarregar_carga(self):
        print(f"O Caminhão {self._marca} está sendo descarregado")