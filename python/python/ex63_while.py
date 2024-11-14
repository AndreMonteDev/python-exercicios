nome = 'Andre Luiz Monte'
nome_tamanho = len(nome)
print(f'{nome_tamanho=}')
contador = 0
while contador < nome_tamanho:
    print(f'*{nome[contador]}', end='')
    contador += 1
print('*', end='')
