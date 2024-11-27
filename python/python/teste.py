import random

cpf_aleatorio = ''

for numero in range(9):
    numero_aleatorio = random.randint(0, 9)
    cpf_aleatorio += str(numero_aleatorio)
    
print(cpf_aleatorio)