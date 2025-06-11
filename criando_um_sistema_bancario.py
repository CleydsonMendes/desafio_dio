# Este é um script simples de um sistema bancário em Python.
# Ele permite depositar, sacar, ver o extrato, fazer transações PIX e sair.

menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] PIX
[0] Sair

=> """

# Variáveis iniciais do sistema
saldo = 0
limite = 500
limite_pix = 250
extrato = ""
numero_saques = 0
numero_pix = 0
LIMITE_SAQUES = 3
QTD_PIX = 3

# Loop principal do programa
while True:
    # Solicita ao usuário que escolha uma opção do menu
    opcao = input(menu)

    # Opção [1]: Depositar
    if opcao == "1":
        try:
            valor = float(input("Informe o valor do depósito: "))
            if valor > 0:
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n"
                print("Depósito realizado com sucesso!")
            else:
                print("Operação falhou! O valor informado é inválido.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

    # Opção [2]: Sacar
    elif opcao == "2":
        try:
            valor = float(input("Informe o valor do saque: "))

            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite
            excedeu_saques = numero_saques >= LIMITE_SAQUES

            if excedeu_saldo:
                print("Operação falhou! Você não tem saldo suficiente.")
            elif excedeu_limite:
                print(f"Operação falhou! O valor do saque excede o limite de R$ {limite:.2f}.")
            elif excedeu_saques:
                print(f"Operação falhou! Número máximo de {LIMITE_SAQUES} saques excedido.")
            elif valor > 0:
                saldo -= valor
                extrato += f"Saque:    R$ {valor:.2f}\n"
                numero_saques += 1
                print("Saque realizado com sucesso!")
            else:
                print("Operação falhou! O valor informado é inválido.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")
    
    # Opção [4]: PIX
    elif opcao == "4":
        try:
            valor = float(input("Informe o valor do PIX: "))

            excedeu_saldo = valor > saldo
            excedeu_limite_pix = valor > limite_pix
            excedeu_pix = numero_pix >= QTD_PIX

            if excedeu_saldo:
                print("Operação falhou! Você não tem saldo suficiente.")
            elif excedeu_limite_pix:
                print(f"Operação falhou! O valor do PIX excede o limite de R$ {limite_pix:.2f}.")
            elif excedeu_pix:
                print(f"Operação falhou! Número máximo de {QTD_PIX} PIX excedido.")
            elif valor > 0:
                saldo -= valor
                extrato += f"PIX:      R$ {valor:.2f}\n"
                numero_pix += 1
                print("PIX realizado com sucesso!")
            else:
                print("Operação falhou! O valor informado é inválido.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

    # Opção [3]: Extrato
    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    # Opção [0]: Sair
    elif opcao == "0":
        print("Saindo do sistema. Obrigado por usar nossos serviços!")
        break

    # Opção inválida
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
