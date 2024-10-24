from Veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca):
        super().__init__(marca)

    def ligar_ar_condicionado(self):
        print(f"O carro {self._marca} está ligando ar condicionado...")