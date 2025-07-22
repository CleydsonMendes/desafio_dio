# Entrada do número de pacientes
try:
    n = int(input().strip())
except ValueError:
    n = 0 # Define n como 0 se a entrada for inválida

# Lista para armazenar pacientes
pacientes = []

# Loop para entrada de dados
for _ in range(n):
  try:
    nome, idade, status = input().strip().split(", ")
    idade = int(idade)
    pacientes.append((nome, idade, status))
  except (ValueError, IndexError):
        # Ignora linhas com formato inválido para tornar o código mais robusto
        continue
lista_ordenada = sorted(pacientes, key=lambda p: (
    0 if p[2] == 'urgente' else 1,  # Critério 1: Status (p[2]). 'urgente' recebe 0.
    0 if p[1] >= 60 else 1,           # Critério 2: Idade (p[1]). Acima de 60 recebe 0.
    -p[1]
))  

# TODO: Ordene por prioridade: urgente > idosos > demais:
nomes_ordenados = [p[0] for p in lista_ordenada]

# TODO: Exiba a ordem de atendimento com título e vírgulas:
string_final_nomes = ", ".join(nomes_ordenados)

print(f"Ordem de Atendimento: {string_final_nomes}")
