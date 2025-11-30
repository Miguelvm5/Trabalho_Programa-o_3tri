from banco import Banco


def menu_principal():
    print("\n--- BANCO ---")
    print("1. Cadastrar conta")
    print("2. Entrar na conta")
    print("3. Sair")
    return input("Escolha uma opção: ").strip()


def menu_conta():
    print("\n--- MENU DA CONTA ---")
    print("1. Sacar")
    print("2. Depositar")
    print("3. Transferir")
    print("4. Ver saldo")
    print("5. Extrato")
    print("6. Sair")
    return input("Escolha uma opção: ").strip()


def main():
    banco = Banco()

    while True:
        opcao = menu_principal()

        if opcao == "1":
            banco.cadastrar_conta()

        elif opcao == "2":
            conta = banco.login()
            if conta:
                while True:
                    escolha = menu_conta()

                    if escolha == "1":
                        try:
                            valor = float(input("Valor do saque: R$ "))
                        except ValueError:
                            print("Valor inválido.")
                            continue
                        conta.sacar(valor)

                    elif escolha == "2":
                        try:
                            valor = float(input("Depósito: R$ "))
                        except ValueError:
                            print("Valor inválido.")
                            continue
                        conta.depositar(valor)

                    elif escolha == "3":
                        numero = input("Conta destino: ")
                        try:
                            valor = float(input("Valor: R$ "))
                        except ValueError:
                            print("Valor inválido.")
                            continue

                        destino = next((c for c in banco._contas if c.numero == numero), None)

                        if destino:
                            conta.transferir(valor, destino)
                        else:
                            print("Conta destino não encontrada.")

                    elif escolha == "4":
                        print(f"Saldo: R$ {conta.saldo:.2f}")

                    elif escolha == "5":
                        print("\n--- EXTRATO ---")
                        for linha in conta.extrato:
                            print(linha)
                        print(f"Saldo atual: R$ {conta.saldo:.2f}")

                    elif escolha == "6":
                        print("Saindo da conta...")
                        break

                    else:
                        print("Opção inválida.")

        elif opcao == "3":
            print("Obrigado por usar nosso sistema bancário.")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
