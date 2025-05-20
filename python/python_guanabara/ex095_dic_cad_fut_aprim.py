# Cadastra jogadores e gols e exibe lista detalhada de aproveitamento (lista com dicionario)

jogadores = []
jogador = {}
continuar = ''
partidas = []
n_partidas = 0
i = 0
while True:
    jogador['nome'] = str(input('Nome do Jogador: '))
    n_partidas = int(input(f'{jogador['nome']}, quantas partidas você jogou? '))
    if n_partidas > 0:
        for i in range(n_partidas):
            partidas.append(int(input(f'Quantos gols na partida {i}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    jogadores.append(jogador.copy())
    partidas.clear()
    continuar = str(input('Continuar? [S/N] '))
    print('-' * 42)
    if continuar in 'Nn':
        break

print('Cod Nome            Gols             Total')
print('-' * 42)

for i, v in enumerate(jogadores):
    gols_str = str(v['gols'])
    print(f"{i:<3} {v['nome']:<15} {gols_str:<20} {v['total']:<4}")
print('-' * 42)

while True:
    opcao = int(input('Mostrar dados de qual jogador? '))
    if opcao == 999:
        break
    if opcao > len(jogadores):
        print(f'ERRO! Não existe jogador com o código {opcao}! Tente novamente')
    else:
        print('-' * 42)
        print(f"-- LEVANTAMENTO DO JOGADOR {jogadores[opcao]['nome']}:")
        for i, v in enumerate(jogadores[opcao]['gols']):
            print(f'No jogo {i} fez {v} gols.')
