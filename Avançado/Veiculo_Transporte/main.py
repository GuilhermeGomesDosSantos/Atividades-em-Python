from Carro import Carro
from Moto import Moto
from Caminhao import Caminhao

carro_1 = Carro("BMW")
moto_1 = Moto("Suzuki")
caminhao = Caminhao("Mercedes")

def main():
    carro_1.ligar_ar_condicionado()
    moto_1.acionar_pedaleira()
    caminhao.descarregar_carga()

if __name__ == "__main__":
    main()