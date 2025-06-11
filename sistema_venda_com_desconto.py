# Dicionário com os valores de desconto
descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00
}

# Entrada do usuário
preco = float(input().strip())
cupom = input().strip()

# TODO: Aplique o desconto se o cupom for válido:

vlr_desconto = preco * descontos[cupom]

vlr_venda = preco - vlr_desconto

print(f"{vlr_venda:.2f}")
