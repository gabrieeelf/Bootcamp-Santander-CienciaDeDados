#AND = para ser True tudo tem que ser True
#OR = para ser True apenas um tem que ser True

print(True and True and True)
print(True and False and True)
print(False and False and False)
print(True or True  or True)
print(True or False  or True)
print(False or False or False)

saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp)

exp2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp2)

conta_normal = saldo >= saque and saque <= limite
conta_especial = conta_especial and saldo >= saque

exp3 = conta_normal or conta_especial
print(exp3)