# 12 - Cachorro e Gato: Crie uma hierarquia de classes onde Cachorro e Gato herdam de Animal. Cada animal deve ter um método fazer_som que retorna o som específico do animal.


from abc import ABC, abstractmethod

class Animal(ABC):
    pass

    @abstractmethod
    def fazer_som():
        pass