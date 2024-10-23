# 11 - Jogo de Dados: Crie uma classe Dado com um método rolar que retorna um valor aleatório entre 1 e 6. Implemente um método mostrar_resultado que exibe o resultado do dado.

from random import randint

class Dado:
    def __init__(self):
        self.resultado = None
    
    def rolar_dado(self):
         self.resultado = randint(1, 6)
         return self.resultado

    def mostrar_resultado(self):
        if self.resultado == None:

            print(f"O Dado ainda não foi jogado!!!")
        else:
            print(f"O valor do Dado é: {self.resultado}")