total = 0
nome = ''
preco = float(0)
qtd_maior_mil = 0
preco_barato = 0
mais_barato = ''
continuar = ''

while True:
    nome = input('Digite o nome do produto: ')
    preco = float(input('Digite o preço do produto: R$ '))
    total += preco
    if preco > 1000:
        qtd_maior_mil += 1
    if preco_barato == 0:
        preco_barato = preco
    if preco < preco_barato:
        mais_barato = nome
        preco_barato = preco
    continuar = input('Continuar [s/n]? ')
    if continuar == 'n':
        break
    elif continuar not in 'sn':
        print('Digita [s] ou [n] por favor.')
print('=' * 30)
print(f'O total de gasto foi: {total:.2f}')
print(f'Quantidade de produtos que custaram mais de R$ 1000: {qtd_maior_mil}')
print(f'Produto mais barato: {mais_barato} - R$ {preco_barato:.2f}')
                    


