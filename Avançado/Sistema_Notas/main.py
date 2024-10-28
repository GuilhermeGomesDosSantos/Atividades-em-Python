from Disciplina import Disciplina
from Aluno import Aluno

disciplina = Disciplina()
aluno = Aluno("Guilherme")

def main():
    aluno.adicionar_disciplinas()
    aluno.listar_disciplina()
    aluno.calcular_media()

if __name__ == "__main__":
    main()