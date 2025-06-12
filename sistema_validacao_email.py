email_usuario = input()

# Verificação 1: Se tiver espaço, já é inválido.

def validar_email(email_usuario):
  if " " in email_usuario:
    return "E-mail inválido"
# Verificação 2: Se NÃO tiver "@", é inválido.
  elif "@" not in email_usuario:
    return "E-mail inválido"
# Verificação 3: Se começa ou termina com "@", é inválido.
  elif email_usuario.startswith("@") or email_usuario.endswith("@"):
    return "E-mail inválido"
# Verificação 4: Lógica do domínio... se falhar, é inválido.
  partes_do_email = email_usuario.split('@')
  dominio = partes_do_email[1]

  if "." not in dominio:
    return "E-mail inválido"
# Se passou por todas as verificações acima, então...
  return "E-mail válido"

# Chama a função, passando o e-mail do usuário como argumento
resultado = validar_email(email_usuario) 

# Imprime o resultado que a função retornou
print(resultado)
