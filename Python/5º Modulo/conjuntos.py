# Set - Elimina elementos duplicados
numeros = ([1, 1, 2, 2, 4, 3, 3, 4])
print(set(numeros))

numeros2 = {1, 2, 2, 3, 4} # Utilizando chaves já retira os duplicados.
print(numeros2)
# print(numeros2[2]) - Dessa forma não é possível acessar um conjunto

# Formas de acessar o conteúdo de um Set:
for numero in numeros2:
    print(numero)

print()

# Enumerate - Quando quero saber o indice que percorro no elemento
carros = {"Gol", "Celta", "Palio"}

for i, carro in enumerate(carros):
    print(f"{i}: {carro}")

print()

# Union - Unifica os elementos

conj_a = {1, 2, 3}
conj_b = {4, 2, 3}

print(conj_a.intersection(conj_b)) # Encontra os valores em comuns dentro dos conjuntos

print()

# Difeference - Tudo que eu tenho em um conjunto que não tem no outro
conj_a = {1, 2, 3}
conj_b = {4, 2, 3}

print(conj_a.difference(conj_b)) 
print(conj_b.difference(conj_a))

print()

# Symetric_difference - Todos os elementos que não estão nos conjuntos
conj_a = {1, 2, 3}
conj_b = {4, 2, 3}

print(conj_a.symmetric_difference(conj_b))

print()

# Issubset - Se um conjunto é um subconjunto = True, basicamente ele identifica se todos os elementos de um conjunto está no outro
conj_a = {1, 2, 3}
conj_b = {1, 4, 2, 3}

print(conj_a.issubset(conj_b))
print(conj_b.issubset(conj_a))

print()

# Isuuperset - Faz a mesma verificação do issubset, só que ao contrario.
conj_a = {1, 2, 3}
conj_b = {1, 4, 2, 3}

print(conj_a.issuperset(conj_b))
print(conj_b.issuperset(conj_a))

print()

# Isdisjoint - Verifica se algum valor está no outro conjunto, caso seja verdadeiro os valores não se repetem

conj_a = {1, 2, 3}
conj_b = {1, 4, 2, 3}
conj_c = {6, 5, 7}

print(conj_a.isdisjoint(conj_b))
print(conj_b.isdisjoint(conj_c))

print()

# Add - Caso o elemento não exista é adicionado ao conjunto
sorteio = {1, 23}

sorteio.add(20)
sorteio.add(20)
sorteio.add(17)
print(sorteio)
print()

# Clear - limpa os elementos
print(sorteio.clear())
print()

# Copy - Copia o conjunto desejado
conj_d = conj_a.copy()
print(conj_d)

# Discard - Descarta o elemento desejado
conj_d.discard(1)
print(conj_d)
print()

# Pop - Retira o último valor do conjunto
conj_d.pop()
print(conj_d)
print()

# Remove - Remove aquele que você deseja, caso não tenha o valor o retorno será de erro.
conj_d.add(1)
print(conj_d)
conj_d.remove(3)
print(conj_d)

print()

# Len - Informa o tamanho do seu conjunto
print(len(conj_a))
print()

# In - Verifica se um elemento está no conjunto
print(1 in conj_a)