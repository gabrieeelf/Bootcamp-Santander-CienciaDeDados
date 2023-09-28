# Append - Serve para inserir um novo valor a lista
lista = []
lista.append(1)
lista.append(2)
lista.append("Teste")
print(lista)

print()

# Copy - Retorna uma lista igual com uma instância diferente
lista_copy = [5, 4, 3, 2, 1]
lista_copy_v2 = lista_copy.copy() # Copiando os mesmos valores para a váriavel, não afetando a lista de origemm

print(lista_copy) 

print(id(lista_copy), id(lista_copy_v2))

lista_copy_v2[0] = 2

print(lista_copy)
print(lista_copy_v2)
print()

# Count - Conta quantas vezes um valor se repete dentro de uma lista
numeros = [1, 1, 1, 2, 1]

print(numeros.count(1))
print()

# Extend - Adiciona novos valores de uma vez, não somente de 1 em 1

numeros.extend([1, 2, 5, 1, 10])
print(numeros)
print()

# Index - Encontra a primeira ocorrênci que o valor se encontra
print(numeros.index(2))
print()

# Pop - Remove sempre o último elemento por natureza, caso você utilize algum parâmetro, remove o mesmo
linguagens = ["Python", "Js", "C", "Java"]
print(linguagens.pop(2))
print(linguagens)
print()

# Remove - Remove elementos da lista, utilizando como parâmetro o próprio elemento
linguagens.remove("Java")
print(linguagens)
print()

# Reverse - Inverte os elementos da lista
numeros.reverse()
print(numeros)
print()

# Sort - Ordena os elementos da lista
numeros.sort() # Do maior para o Menor
print(numeros)

numeros.sort(reverse=True) # Do menor para o maior
print(numeros)

linguagens.sort(key=lambda x: len(x)) # Do menor para o maior em tamanho
print(linguagens)

linguagens.sort(key=lambda x: len(x), reverse=True) # Do maior para o menor em tamanho
print(linguagens)

print()

# Len - Encontra o tamanho da lista
linguagens = ["python", "js", "c", "java", "csharp"]

print(len(linguagens))  # 5
print()

# Sorted - Serve para ordenar
linguagens = ["python", "js", "c", "java", "csharp"]

print(sorted(linguagens, key=lambda x: len(x)))  # ["c", "js", "java", "python", "csharp"]
print(sorted(linguagens, key=lambda x: len(x), reverse=True))  # ["python", "csharp", "java", "js", "c"]