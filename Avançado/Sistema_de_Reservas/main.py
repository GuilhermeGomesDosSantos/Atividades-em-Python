from Reserva import Reserva

quarto_1 = Reserva()

def main():
    quarto_1.reservar("Quarto 1")
    # quarto_1.listar_quartos()
    quarto_1.verificar_dispobilidade("Quarto 2")
    quarto_1.verificar_dispobilidade("Quarto 1")

if __name__=="__main__":
    main()