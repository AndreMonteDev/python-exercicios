# Cadastra nome de jogadores e gols por partida e depois exibe

aproveitamento ={}
partidas = []
aproveitamento['nome'] = str(input('Nome do Jogador: '))
qtd_partidas = int(input(f'Quantas partidas {aproveitamento["nome"]} jogou? '))
p = 0
if qtd_partidas != 0:
    for p in range(qtd_partidas):
        partidas.append(int(input(f'Quantos gols na partida {p}? ')))
    aproveitamento['gols'] = partidas[:]
    aproveitamento['total'] = sum(partidas)

print('-=' * 40)
print(aproveitamento)
print('-=' * 40)
for k, v in aproveitamento.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 40)
print(f'O jogador {aproveitamento["nome"]} jogou {qtd_partidas} partidas.')
for i, gol in enumerate(partidas):
    print(f'    => Na partida {i}, fez {gol} gols.')
print(f'Foi um total de {aproveitamento["total"]} gols.')  