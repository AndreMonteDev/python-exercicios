filmes = {'nome': 'Star Wars', 'tempo' : 96, 'classificacao': 14, 'nota' : 5.5}

print(filmes)
print(filmes.items())
print(filmes.keys())
print(filmes.values())
print('CHAVE          VALOR')
for k, v in filmes.items():
    print(f'{k:<14} {v}')

print(filmes['nome'])