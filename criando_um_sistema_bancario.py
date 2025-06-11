menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[p] PIX
[q] Sair

=> """

saldo = 0
limite = 500
limite_pix = 250
extrato = ""
numero_saques = 0
numero_pix = 0
LIMITE_SAQUES = 3
QTD_PIX = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
    
    elif opcao == "p":
        valor = float(input("Informe o valor do pix: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite_pix

        excedeu_pix = numero_pix >= QTD_PIX

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do pix excede o limite.")

        elif excedeu_pix:
            print("Operação falhou! Número máximo de pix excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Pix: R$ {valor:.2f}\n"
            numero_pix += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
