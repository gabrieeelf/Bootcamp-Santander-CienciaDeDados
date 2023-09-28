# Declarando Tuplas

frutas = ("Laranja", "Pera", "Uva",) # Boa prática colocar uma virgula ao final dos valores
print(frutas[1]), "\n"

letras = tuple("Python")
print(letras[-2]) # Busca o elemento de forma invertida

numeros = tuple([1, 2, 3, 4])

pais = ("Brasil",)

matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c"),
)

print(matriz[0])
print(matriz[0][0])
print(matriz[0][-1])
print(matriz[-1][-1])

tupla = ("P", "y", "t", "h", "o", "n")
print(tupla[:-1])