# Crie uma classe Calendario para adicionar, remover e listar eventos.

from Evento import Evento

class Calendario:
    def __init__(self):
        self._lista_eventos = []

    def adicionar_evento(self, nome, data, local):
        evento = Evento (nome, data, local)

        self._lista_eventos.append(evento)
        print(f"Evento: {evento._nome} - Data: {evento._data} - Endereço: {evento._local}")

    def listar_eventos(self):
        if not self._lista_eventos:
            print("A lista de eventos está vazia")
        for i, evento in enumerate (self._lista_eventos, start =1):
            print(f"{i} - Evento: {evento._nome} - Data: {evento._data} - Endereço: {evento._local}")

    def remover_eventos(self, nome_evento):
        for evento in self._lista_eventos:
            if evento._nome == nome_evento:
                self._lista_eventos.remove(evento)
                print(f"O evento {nome_evento} foi removido com sucesso")
                return
            
        print(f"Evento: {nome_evento} não foi encontrado")