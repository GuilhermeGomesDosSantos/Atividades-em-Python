# 25 - Sistema de Notas: Implemente uma classe Disciplina que armazena notas de alunos e calcula a média. Crie uma classe Aluno que herda de Disciplina.

from abc import ABC


class Disciplina(ABC):
    def __init__(self):
        self.disciplinas = {}

    def adicionar_disciplinas(self):
        while True:

            nova_disciplina = input("Nome da Disciplina: ").strip()

            if not nova_disciplina:
                print("Disciplina invalida, digite novamente !!!")
                continue

            nova_nota = input(f"Nota da disciplina '{nova_disciplina}' ").strip()

            try:
                nova_nota = float(nova_nota)
            except ValueError:
                print(
                    f"Nota da disciplina {nova_disciplina} está errada, digite novamente"
                )
                continue

            if nova_nota > 10 or nova_nota < 1:
                print(
                    f"Nota da disciplina {nova_disciplina} está errada, digite novamente"
                )
                continue

            self.disciplinas[nova_disciplina] = float(nova_nota)
            print(f"Disciplina {nova_disciplina} com a nota {nova_nota} foi adicionada")

            continuar = (
                input("Deseja adicionar outra disciplina ? s / n -> ").strip().lower()
            )
            if continuar != "s" and continuar != "sim":
                break

    def listar_disciplina(self):
        if not self.disciplinas:
            print("A lista está vazia !!!")

        for disciplina, nota in self.disciplinas.items():
            print(f"{disciplina}, nota: {nota}")

    def calcular_media(self):
        total = 0
        for nota in self.disciplinas.values():
            total += nota
        media = total / len(self.disciplinas) if self.disciplinas else 0
        print(f"A média é {media}")