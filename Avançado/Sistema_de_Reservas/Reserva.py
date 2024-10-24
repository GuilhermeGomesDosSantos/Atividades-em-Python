# 17 - Sistema de Reservas: Implemente uma classe Reserva para gerenciar reservas em um hotel. A classe deve ter métodos para reservar, cancelar e verificar disponibilidade.

class Reserva:
    def __init__(self):
        self.dicionario_quarto = [{'nome': f'Quarto {i}', 'disponivel': True} for i in range(1, 11)]

    def listar_quartos(self):
        print("Lista de quartos:")
        for quarto in self.dicionario_quarto:
            status = "Disponível" if quarto['disponivel'] else "Reservado"
            print(f"{quarto['nome']} - Status: {status}")

    def reservar(self, quarto_selecionado):
        for quarto in self.dicionario_quarto:
            
            if quarto_selecionado == quarto["nome"]:
                if quarto['disponivel'] == True:
                    quarto['disponivel'] = False
                    print(f'O quarto {quarto["nome"]}, foi reservado')
                else:
                    print(f"O quarto '{quarto['nome']}, já está reservado")
                return

        print(f"O quarto '{quarto_selecionado}', não foi encontrado")

    def cancelar(self, quarto_selecionado):
        for quarto in self.dicionario_quarto:
            if quarto_selecionado == quarto["nome"]:
                if quarto['disponivel'] == False:
                    quarto['disponivel'] = True
                    print(f"A reserva do quarto {quarto["nome"]}, foi cancelada!!!")
                    return

                else:
                    print(f"O quarto {quarto['nome']}, ainda não foi reservado")
                    return
                
        print(f"O quarto '{quarto_selecionado}', não foi encontrado!!!")

    def verificar_dispobilidade(self, quarto_selecionado):
        for quarto in self.dicionario_quarto:
            if quarto_selecionado == quarto["nome"]:
                print(f"Status quarto - {quarto['nome']}")
                disponivel = 'disponivel' if quarto['disponivel'] else 'reservado!!!'
                print(f"A disponibilidade do quarto {quarto['nome']} esta '{disponivel}'")
                return
        
        print(f"O quarto {quarto_selecionado}, não foi encontrado!!!")