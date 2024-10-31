# Sistema de Cadastro de Alunos: Implemente uma classe Aluno com nome e nota. O menu deve permitir cadastrar alunos, listar todos os alunos e mostrar a média das notas.
from os import system, name


class Aluno:
    def __init__(self):
        self.lista_alunos = {}

    def limpar_tela(self):
        if name == "nt":
            _ = system("cls")
        else:
            _ = system("clear")

    def menu_opcao(self):
        while True:
            self.limpar_tela()
            print(
                """
            Escolha uma opção
            1 - Cadastrar Aluno
            2 - Listar alunos
            3 - Mostrar média das notas
            4 - Sair
            """
            )
            opcao = input("Escolha uma opção: ").strip()

            if opcao == "1":
                self.limpar_tela()

                self.cadastrar_aluno()

            elif opcao == "2":
                self.limpar_tela()

                self.listar_alunos()

            elif opcao == "3":
                self.limpar_tela()
                self.mostrar_media_nota()

            elif opcao == "4":
                self.limpar_tela()
                print("Saindo...")
                break

    def cadastrar_aluno(self):
        while True:
            self.limpar_tela()
            nome_aluno = input("Digite o nome do aluno: ")

            if not nome_aluno:
                print("Por favor digite o nome do aluno direito")
                continue

            materia = []

            while True:
                ## vai ter que criar uma lista pra materia e nota
                nome_materia = input(f"Digite o nome da materia do aluno {nome_aluno}: ")

                if not nome_materia:
                    print("Por favor digite a materia do aluno corretamente")
                    continue

                while True:
                    nota_materia = input(f"Digite a nota da matéria {nome_materia}: ").strip()

                    if nota_materia.isnumeric():
                        nota_materia = int(nota_materia)
                        materia.append({"materia": nome_materia, "nota": nota_materia})
                        break
                    else:
                        print("Por favor, digite uma nota válida.")

                continuar = input("Você deseja adicionar outra matéria? (s/n): ").strip().lower()

                if continuar in ('n', 'não'):
                    self.lista_alunos[nome_aluno] = materia
                    self.limpar_tela()
                    return
                
                elif continuar != 's' or continuar != 'sim':
                    return



    def listar_alunos(self):
        if not self.lista_alunos:
            print("A lista de alunos está vazia")

        for aluno, materias in self.lista_alunos.items():
            print(f"\nAluno: {aluno}")
            for materia in materias:
                print(f" - Matéria: {materia['materia']}, Nota: {materia['nota']}")
            print('-' * 30)

        input("\nPressione 'Enter' para voltar ao menu")

    def mostrar_media_nota(self):
        if not self.lista_alunos:
            print("A lista de alunos está vazia")
            input("\nDigite 'Enter' para voltar ao menu")
            
        for aluno, materias in self.lista_alunos.items():
            total_notas = 0
            quantidade_materias = len(materias)

            for materia in materias:
                total_notas += materia['nota']
            
            media = total_notas / quantidade_materias
            print(f"Aluno: {aluno} - Média das notas: {media:.2f}")

        input("Pressione enter para sair")