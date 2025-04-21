tabela = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9, 'Estojo', 25, 'Transferidor', 4.2, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.9)

print('_' * 39)
print(('LISTAGEM DE PREÇOS').center(40))
print('_' * 39)

for cont in range(0, len(tabela)):
    if cont % 2 == 0:
        print(f'{tabela[cont]:.<30}', end='') 
    else:
        print(f'R${tabela[cont]:>7.2f}')
print('_' * 39)

