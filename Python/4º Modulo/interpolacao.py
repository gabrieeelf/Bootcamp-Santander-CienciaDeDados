nome = "Gabriel"
idade = 20
profissao = "Trainne de TI"
linguagem = "Python"


print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s." % (nome, idade, profissao, linguagem))

print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}.".format(nome, idade, profissao, linguagem))

print("Olá, me chamo {1}. Eu tenho {2} anos de idade, trabalho como {3} e estou matriculado no curso de {0}.".format(linguagem, nome, idade, profissao))

# MÉTODO FORMAT

print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}."
      .format(
            nome = nome, idade = idade, profissao = profissao, linguagem = linguagem))

print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.")

print()

PI = 3.14159

print(f"Valor de PI: {PI:.2f}")
print(f"Valor de PI: {PI:10.2f}")

dados = {"nome": "Gabriel Queiroz", "idade": 20}

print("Nome: {nome} Idade: {idade}".format(**dados))