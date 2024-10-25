from Projeto import Projeto

projeto_1 = Projeto("Projeto X")

def main():
    projeto_1.adicionar_membros("Guilherme")
    projeto_1.adicionar_tarefa("Testando codigo")
    projeto_1.listar_tarefas()

if __name__ == "__main__":
    main()