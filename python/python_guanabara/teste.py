lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 3, 4, 2, 2, 4, 5, 3, 1]
lista.sort()
print(lista)
while 2 in lista:
    lista.remove(2)
print(lista)
for c, v in enumerate(lista):
    print(f'({c}) {v}')
