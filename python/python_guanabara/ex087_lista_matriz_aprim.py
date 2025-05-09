# recebe numeros, inclui numa matriz 3x3, exibe a soma dos valores pares, a soma dos valores da 3ª coluna e o maior valor da 2ª coluna

matriz = []
valores = []
soma_pares = 0
soma_coluna3 = 0
for x in range(3):
    for y in range(3):
        valores.append(int(input(f'Digite o valor para [{x, y}]: ')))
    matriz.append(valores[:])
    valores.clear()
print('=' * 30)
for i in range(3):
    for j in range(3):
        print(f'[ {matriz[i][j]:^5} ]', end='')
        if (matriz[i][j]) % 2 == 0:
            soma_pares += matriz[i][j]
    soma_coluna3 += matriz[i][2]
    print('')
print('=' * 30)
print(f'Soma de valores pares: {soma_pares}')
print('=' * 30)
print(f'Soma de valores da 3ª coluna: {soma_coluna3}')
print('=' * 30)
print(f'O maior valor da 2ª linha: {max(matriz[1])}')
