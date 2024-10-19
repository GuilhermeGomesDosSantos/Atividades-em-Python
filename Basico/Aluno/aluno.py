# Aluno: Crie uma classe Aluno com atributos nome e notas. Adicione um método media que calcula a média das notas do aluno.

class Aluno:
    def __init__(self, nome, notas):
        self._nome = nome
        self._notas = notas

        if isinstance(notas, list):
            self._notas = notas

        else:
            self._notas = [notas]
            
    def media(self):
        if len(self._notas) == 0:
            print('Até o momento nenhuma nota foi fornecida')
        else:
            media_nota = sum(self._notas)/ len(self._notas)
            print(f'A media da nota do Aluno {self._nome} é: {media_nota:.2f}')

        print(f'Total é: {media_nota}')