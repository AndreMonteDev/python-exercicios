# cadastra 7 valores e adiciona em 2 listas separados por impares e pares dentro de outra lista

numeros = [[],[]]
valor = 0

for n in range(7):
    valor = int(input(f'Digite {n}o valor: '))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)
numeros[0].sort()
numeros[1].sort()
print('-=' * 30)
print(f'Os valores pares digitados foram: {numeros[0]}')
print(f'Os valores ímpares digitados foram: {numeros[1]}')


