# recebe nome e num de gols de jogador e exibe ficha (mesmo que não tenha preenchido algum valor)

def ficha(nome='desconhecido', gols=0):
    return print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')

nome = str(input('Nome do Jogador: '))
gols = (input('Número de Gols: '))

ficha(nome, gols)
