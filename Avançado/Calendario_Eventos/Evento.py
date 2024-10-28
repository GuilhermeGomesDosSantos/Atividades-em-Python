# Calendário de Eventos: Crie uma classe Evento com atributos nome, data e local. Crie uma classe Calendario para adicionar, remover e listar eventos.

class Evento:
    def __init__(self, nome, data, local):
        self._nome = nome
        self._data = data
        self._local = local
