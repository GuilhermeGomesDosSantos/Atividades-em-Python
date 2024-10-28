from Calendario import Calendario
from Evento import Evento

calendario_1 = Calendario()
# evento = Evento("Evento teste", "30/10/2024", "Rua teste desafio")
def main():
    calendario_1.adicionar_evento("Evento teste 1", "30/10/2024", "Rua teste desafio")
    calendario_1.adicionar_evento("Evento teste 2", "30/10/2024", "Rua teste desafio")
    calendario_1.adicionar_evento("Evento teste 3", "30/10/2024", "Rua teste desafio")
    calendario_1.listar_eventos()

    calendario_1.remover_eventos("Evento teste 1")
    calendario_1.listar_eventos()
    calendario_1.remover_eventos("Teste")
    calendario_1.remover_eventos("Evento teste 2")
    calendario_1.listar_eventos()

if __name__ == "__main__":
    main()