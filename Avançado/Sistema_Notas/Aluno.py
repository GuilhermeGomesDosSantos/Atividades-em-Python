from Disciplina import Disciplina

class Aluno(Disciplina):

    def __init__(self, nome):
        super().__init__()
        self._nome = nome

    def listar_disciplina(self):
        print(f"Lista de disciplinas do Aluno {self._nome}")
        return super().listar_disciplina()
    
    def calcular_media(self):
        print(f"A media do aluno {self._nome} é:")
        return super().calcular_media()