lista = []
for c, v in enumerate(range(0, 5)):
    lista.append(int(input(f'Digite um valor da posição {c}: ')))

maior = max(lista)
menor = min(lista)

print(f'Você digitou os valores: {lista}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for c, v in enumerate(lista):
    if maior == v:
        print(f'{c}...', end='')
print('')
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for c, v in enumerate(lista):
    if menor == v:
        print(f'{c}...', end='')
