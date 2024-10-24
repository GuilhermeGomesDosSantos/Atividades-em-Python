# 18 - Sistema de Votação: Crie uma classe Votacao que permita registrar votos para candidatos. Adicione métodos para calcular o vencedor e exibir resultados.

class Votacao:
    def __init__(self):
        self.lista_candidatos = [{'nome' : f'Candidato{i}', 'votos': 0} for i in range(1, 4)]

    def exibir_resultados(self):
        for candidato in self.lista_candidatos:
            print(f"Candidato {candidato["nome"]} - Total de votos = {candidato["votos"]}")

    def vencedor(self):
        total_votos = sum(candidato['votos'] for candidato in self.lista_candidatos)
        
        if total_votos == 0:
            print("Até o momento não foi realizado nenhum voto")
        else:
            # Encontra o candidato com mais votos
            vencedor = max(self.lista_candidatos, key=lambda c: c['votos'])
            print(f"O vencedor é {vencedor['nome']} com {vencedor['votos']} votos")


    def votar(self, nome_candidato):
        votar = 1
        for candidato in self.lista_candidatos:
            if nome_candidato == candidato["nome"]:
                candidato["votos"] += 1
                print("Votação concluida com sucesso")
                return
        
        print(f"O Candidato '{nome_candidato}' não foi encontrado!!!")