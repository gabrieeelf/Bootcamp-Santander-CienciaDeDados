"""texto = input("Informe um texto: ")
vogais = "AEIOU"

for letra in texto:
    if letra.upper() in vogais:
        print(letra, end="")
else:
    print()
    print("Executa no final do laço")"""


# Utilizando range com for

for numero in range(0, 11):
    print(numero, end=" ")

print()

for numero in range(0, 51, 5):
    print(numero, end=" ")

print()

# While

opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair: "))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo extrato...")

else:
    print("Obrigado por usar nosso sistema bancário!")
    print()


while True:
    numeroV2 = int(input("Informe um número: "))

    if numeroV2 == 10:
        break

    print(numeroV2)


for numeroV3 in range(100):

    if numeroV3 % 2 == 0:
        continue

    print(numeroV3, end=" ")