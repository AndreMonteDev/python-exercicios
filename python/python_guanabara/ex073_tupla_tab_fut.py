# Tabela do Brasileirão
tabela = ('Flamengo', 'Palmeiras', 'Ceará', 'Juventude', 'Fluminense', 'Vasco', 'Internacional', 'Fortaleza', 'Corinthians', 'Botafogo', 'Bragantino', 'Cruzeiro', 'Grêmio', 'Bahia', 'São Paulo', 'Alético-MG', 'Mirassol', 'Santos', 'Vitória', 'Sport')

print('=' * 21)
print('TABELA DO BRASILEIRÃO')
print('=' * 21)

print('Lista de times:')
print(tabela)
print('=' * 21)

print('Primeiros 5 colocados:')
print(tabela[0:5])
print('=' * 21)

print('Últimos 4 colocados:')
print(tabela[-4:])
print('=' * 21)
 
tabela_ordem = sorted(tabela)
print('Times em ordem alfabética: ')
print(tabela_ordem)
print('=' * 21)

print('O Corinthians está na posição: ')
print(tabela.index('Corinthians') + 1)
