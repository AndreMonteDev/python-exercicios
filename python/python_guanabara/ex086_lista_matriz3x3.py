matriz = []
valores = []
for x in range(3):
    for y in range(3):
        valores.append(int(input(f'Digite o valor para [{x, y}]: ')))
    matriz.append(valores[:])
    valores.clear()

for i in range(3):
    for j in range(3):
        print(f'[ {matriz[i][j]:^5} ]', end='')
    print('')