curso = "Python"

print(curso.upper()) # Tudo maiúsculo

print(curso.lower()) # Tudo minúsculo

print(curso.title()) # Primeira letra Maiúscula

print()

espaco = "  Python  "

print(espaco.strip()) # Remove o espaço da direita e esquerda

print(espaco.lstrip()) # Remove o espaço da esquerda

print(espaco.rstrip()) # Remove o espaço da direita

print()

# JUNÇÕES E CENTRALIZAÇÃO   

print(curso.center(10, "#")) # Centraliza o texto a partir do número de caracteres e simbolo

print(".".join(curso)) # Percorre a string colocando o que você informar