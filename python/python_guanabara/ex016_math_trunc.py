import math

n = float(input('Digite um numero decimal: '))

print(f'A parte inteira do número {n} é {math.trunc(n)}')

print(f'O arrendondamento acima do número {n} é {math.ceil(n)}')

print(f'O arredendamento abaixo do número {n} é {math.floor(n)}')
