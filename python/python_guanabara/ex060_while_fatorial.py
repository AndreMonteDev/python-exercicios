num = int(input('Digite um número: '))
c = num - 1
fatorial = num
while c > 0:
    fatorial *= c
    c -= 1
print(f'O fatorial de {num} é {fatorial}.')
