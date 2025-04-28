# cadastra nome e peso, lista quantas pessoas cadastradas, pessoas mais pesadas e pessoas mais leves

pessoas = []
dados = []
continuar = ''
n_pessoas = 0
leves = 0
pesadas = 0
p_leves = []
p_pesadas = []
while continuar != 'n':
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    n_pessoas += 1
    continuar = input('Continuar? [S/N] ')

for p in pessoas:
    if leves == 0 or p[1] <= leves:
        leves = p[1]
    if pesadas == 0 or p[1] >= pesadas:
        pesadas = p[1]


print(pessoas)
print(pesadas)
print(leves)

