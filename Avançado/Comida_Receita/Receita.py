# 26 - Comida e Receita: Crie uma classe Receita com atributos nome e ingredientes. Adicione métodos para adicionar ingredientes e exibir a receita.


class Receita:
    # def __init__(self, nome, ingredientes):
    def __init__(self):
        self.lista_receita = {}

    def adicionar_ingredientes(self):
        while True:
            nome_receita = input("Nome da receita: ").strip()

            if not nome_receita:
                print("Nome da receita foi digitado de maneira errada!!!")
                continue

            ingredientes = []

            while True:
                nome_ingrediente = input(f"Informe o igrediente(s) para a receita de {nome_receita}: ").strip()

                if not nome_ingrediente:
                    print(f"O igrediente para a receita {nome_receita} foi digitado de maneira errada")
                    continue

                else:
                    print(f"O ingrediente {nome_ingrediente} foi adicionado na receita {nome_receita}")
                    ingredientes.append(nome_ingrediente)

                while True:
                    continuar = input("Deseja continuar adicionando outros ingredientes à receita? [s / n]: ").strip().lower()
                    
                    if continuar == "n" or continuar == "não":
                        break

                    elif continuar == "s" or continuar == "sim":
                        break

                    else:
                        print("Por favor digite uma das opções: 's' para continuar ou 'n' para sair.")

                if continuar == "n" or continuar == "não":
                    break

            self.lista_receita[nome_receita] = ingredientes
            print(f"Receita '{nome_receita}' foi salva com os ingredientes: {', '.join(ingredientes)}")

            
            while True:

                nova_receita = input("Deseja adicionar uma nova receita ? [s / n]: ").strip().lower()

                if nova_receita == "n" or nova_receita == "não":
                    return

                elif nova_receita == "s" or nova_receita == "sim":
                    break
                
                else:
                    print("Por favor digite algumas das opções\ns -> para Continuar adicionando\nn-> para Sair")
            
