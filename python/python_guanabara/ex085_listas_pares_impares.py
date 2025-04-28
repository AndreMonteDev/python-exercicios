lista = []
pares = []
impares = []
for v in range(7):
    valor = int(input(f'Digite o valor {v}: '))
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)
lista.append(pares[:])
lista.append(impares[:])

pares_ordenados = sorted(lista[0])
impares_ordenados = sorted(lista[1])
print('-=' * 40)
print(f'Os valores pares digitados foram: {pares_ordenados}')
print(f'Os valores impares digitados foram: {impares_ordenados}')


           
