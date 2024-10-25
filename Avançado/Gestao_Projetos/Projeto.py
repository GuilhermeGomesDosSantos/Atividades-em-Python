# 22 - Gestão de Projetos: Crie uma classe Projeto com atributos nome e equipe (lista de membros). Adicione métodos para adicionar membros e listar tarefas.

class Projeto:
    def __init__(self, nome):
        self._nome = nome
        self._equipe = []
        self._lista_tarefas = []

    def adicionar_membros(self, nome_membro):
        self._equipe.append(nome_membro)
        print(f"O membro {nome_membro} foi adicionado a equipe {self._nome}")

    def adicionar_tarefa(self, tarefa):
        self._lista_tarefas.append(tarefa)
        print(f"A tarefa {tarefa} foi adicionada!!!")
        
    def listar_tarefas(self):
        if not self._lista_tarefas:
            print("A lista está vazia!!!")

        print(f"Lista de Tarefas!!!")
        for i, tarefa in enumerate (self._lista_tarefas, start = 1):
            print(f"{i} - {tarefa}")