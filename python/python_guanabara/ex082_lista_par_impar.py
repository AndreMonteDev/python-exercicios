# Inclui valores em uma lista, lista valores pares e valores impares

lista = []
pares = []
impares = []
while True:
    v = int(input('Digite um valor: '))
    lista.append(v)
    continuar = input('Quer continuar? [S/N] ')
    if continuar in 'Nn':
        break

for v in lista:
    if v % 2 == 0:
        pares.append(v)
    if v % 2 != 0:
        impares.append(v)

print('=' * 40)
print(f'Valores digitados: {lista}')
print(f'Valores impares: {impares}')
print(f'Valores pares: {pares}')