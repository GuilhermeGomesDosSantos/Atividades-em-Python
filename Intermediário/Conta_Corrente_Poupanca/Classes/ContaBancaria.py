# 7 - Conta Corrente e Conta Poupança: Crie uma hierarquia de classes onde ContaCorrente e ContaPoupanca herdam de ContaBancaria. Adicione métodos específicos para cada tipo de conta.

from abc import ABC, abstractmethod

class ContaBancaria(ABC):
    def __init__(self, titular, saldo, n_conta):
        self._titular = titular
        self._saldo = saldo
        self._n_conta = n_conta
        self._status = True  # True significa ativa
