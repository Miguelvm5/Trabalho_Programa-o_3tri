from cliente import Cliente
from conta import ContaCorrente, ContaPoupanca


class Banco:
    def __init__(self):
        self._contas = []

    def cadastrar_conta(self):
        print("\n--- Cadastro de Conta ---")

        nome = input("Nome do cliente: ")
        senha = input("Senha (sem espaços): ")

        if " " in senha:
            print("Erro: A senha não pode conter espaços.")
            return

        try:
            saldo = float(input("Saldo inicial: R$ "))
            if saldo < 0:
                print("Saldo inválido.")
                return
        except ValueError:
            print("Saldo inválido.")
            return

        cliente = Cliente(nome, senha)

        print("\nTipo de conta:")
        print("1 - Conta Corrente")
        print("2 - Conta Poupança")

        while True:
            tipo = input("Escolha (1 ou 2): ")
            if tipo in ("1", "2"):
                break
            print("Opção inválida! Escolha entre 1 ou 2.")

        if tipo == "1":
            conta = ContaCorrente(cliente, saldo)
        else:
            conta = ContaPoupanca(cliente, saldo)

        self._contas.append(conta)
        print(f"\nConta criada! Número: {conta.numero}")

    def login(self):
        num = input("Número da conta: ")
        senha = input("Senha: ")

        destino = next(
            (c for c in self._contas if c.numero == num and c._cliente.validar_senha(senha)),
            None
        )

        if destino:
            print(f"\nBem-vindo(a), {destino.titular}!")
            return destino

        print("Conta ou senha inválida.")
        return None
