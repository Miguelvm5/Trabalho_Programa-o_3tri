from abc import ABC, abstractmethod
import random


class Conta(ABC):
    def __init__(self, cliente, saldo=0):
        if saldo < 0:
            raise ValueError("Saldo inicial não pode ser negativo.")

        self._numero = str(random.randint(100000, 999999))
        self._cliente = cliente
        self._saldo = saldo
        self._extrato = []

    @property
    def numero(self):
        return self._numero

    @property
    def nome_cliente(self):
        return self._cliente.nome

    @property
    def saldo(self):
        return self._saldo

    @property
    def extrato(self):
        return self._extrato

    def depositar(self, valor):
        if valor <= 0:
            print("Valor inválido.")
            return

        self._saldo += valor
        self._extrato.append(f"Depósito: +R$ {valor:.2f}")
        print(f"Depósito realizado! Saldo: R$ {self._saldo:.2f}")

    @abstractmethod
    def sacar(self, valor):
        pass

    @abstractmethod
    def transferir(self, valor, conta_destino):
        pass


class ContaCorrente(Conta):
    TAXA_SAQUE = 1.50
    TAXA_TRANSFERENCIA = 2.00

    def sacar(self, valor):
        total = valor + ContaCorrente.TAXA_SAQUE

        if valor <= 0:
            print("Valor inválido.")
            return

        if self._saldo >= total:
            self._saldo -= total
            self._extrato.append(
                f"Saque: -R$ {valor:.2f} (Taxa: {ContaCorrente.TAXA_SAQUE:.2f})"
            )
            print(f"Saque realizado! Saldo atual: R$ {self._saldo:.2f}")
        else:
            print("Saldo insuficiente.")

    def transferir(self, valor, conta_destino):
        total = valor + ContaCorrente.TAXA_TRANSFERENCIA

        if valor <= 0:
            print("Valor inválido.")
            return

        if self._saldo >= total:
            self._saldo -= total
            conta_destino._saldo += valor

            self._extrato.append(
                f"Transferência para {conta_destino.numero}: -R$ {valor:.2f} "
                f"(Taxa: {ContaCorrente.TAXA_TRANSFERENCIA:.2f})"
            )
            conta_destino._extrato.append(
                f"Transferência de {self.numero}: +R$ {valor:.2f}"
            )
            print("Transferência realizada com sucesso!")
        else:
            print("Saldo insuficiente.")


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if valor <= 0:
            print("Valor inválido.")
            return

        if self._saldo >= valor:
            self._saldo -= valor
            self._extrato.append(f"Saque: -R$ {valor:.2f}")
            print(f"Saque concluído! Saldo: R$ {self._saldo:.2f}")
        else:
            print("Saldo insuficiente.")

    def transferir(self, valor, conta_destino):
        if valor <= 0:
            print("Valor inválido.")
            return

        if self._saldo >= valor:
            self._saldo -= valor
            conta_destino._saldo += valor

            self._extrato.append(
                f"Transferência para {conta_destino.numero}: -R$ {valor:.2f}"
            )
            conta_destino._extrato.append(
                f"Transferência de {self.numero}: +R$ {valor:.2f}"
            )
            print("Transferência feita!")
        else:
            print("Saldo insuficiente.")
