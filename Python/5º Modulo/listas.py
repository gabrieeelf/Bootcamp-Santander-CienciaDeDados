frutas = ["Maça", "Banana", "Abacate"]
frutas[0] #Maça
frutas[2] #Banana

# Print com as posições das Frutas
print(frutas, "\n", frutas[0], "\n", frutas[2])

for fruta in frutas:
    print(fruta, "\n")

# Com o list() a variável recebe como valor cada letra
curso = list("Python")

print(curso)

# Atribuindo uma matriz
matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

print(matriz)


numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

# Percorrendo somente os números pares da lista
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print(pares)

# Outra forma de percorrer somente os números pares da lista
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]

print(pares)