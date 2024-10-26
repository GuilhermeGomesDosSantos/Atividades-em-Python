from Baralho import Baralho

baralho = Baralho()

def main():
    baralho.embaralhar()
    mao = baralho.distribuir(5)
    print("Cartas na mão:", [str(carta) for carta in mao])
    mao = baralho.distribuir(7)
    print("Cartas na mão:", [str(carta) for carta in mao])
    print(f"Cartas restantes no baralho {len(baralho.cartas)}")

if __name__ == "__main__":
    main()