menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
[nu] Novo_usuario
[nc] Nova_Conta

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

contas = []
AGENCIA = "0001"

def depositar (saldo, valor, extrato,/):
          if valor > 0:
              saldo += valor
              extrato += f"Depósito: R$ {valor:.2f}\n"

          else:
              print("Operação falhou! O valor informado é inválido.")

          return saldo, extrato

def sacar (*, saldo, valor, extrato, limite, numero_saques, limite_saques):
      
        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= limite_saques

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

        else:
            print("Operação falhou! O valor informado é inválido.")

        return (saldo, extrato, numero_saques)

def exibir_extrato (saldo, / , * , extrato):

    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


usuarios = []

def filtrar_usuario (cpf, usuarios):
    for usuario in usuarios:
      if usuario['cpf']==cpf:
        return usuario
    return None

def criar_usuario (usuarios):
    cpf = input("Informe o CPF (somente números): ")

    usuario_existente = filtrar_usuario (cpf, usuarios)

    if usuario_existente:
      print("\n@@@ Já existe usuário com esse CPF! @@@")
      return

    nome = input("Informe o nome: ")
    data_nascimento  = input("Informe a data de nascimento: ")
    endereco = input("Informe o endereço: ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")


def criar_conta (contas, usuarios, agencia):
    cpf = input("Informe o CPF do usuário: ")  
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        numero_conta = len(contas) + 1
        conta = {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

        contas.append(conta)
      
        print("\n=== Conta criada com sucesso! ===")
        return # Adicionado para clareza

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")

while True:

    opcao = input(menu)

    if opcao == 'd':
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = depositar(saldo, valor, extrato)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato, numero_saques = sacar(
            saldo=saldo, 
            valor=valor,
            extrato=extrato, 
            limite=limite,
            numero_saques=numero_saques,
            limite_saques=LIMITE_SAQUES,
            )

    elif opcao == "e":
        exibir_extrato (saldo, extrato=extrato,)

    elif opcao == "q":
        break
    
    elif opcao == "nu":
        criar_usuario(usuarios)
    
    elif opcao == "nc":
        criar_conta(AGENCIA, contas, usuarios)

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
