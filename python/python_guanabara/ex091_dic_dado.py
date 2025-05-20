# sorteia 4 numeros de dado(1 a 6) e ordena por ordem de quem tirou o maior
import time
import random
import operator

ranking = []
jogador1 = random.randint(1, 6)
jogador2 = random.randint(1, 6)
jogador3 = random.randint(1, 6)
jogador4 = random.randint(1, 6)

jogo = {'jogador1': jogador1, 'jogador2': jogador2, 'jogador3': jogador3, 'jogador4': jogador4}

ranking = sorted(jogo.items(), key=operator.itemgetter(1), reverse=True)

for k, v in jogo.items():
    time.sleep(1)
    print(f"{k} tirou {v}")

print('=' * 30)
print('** Resultado **')
for i, v in enumerate(ranking):
    time.sleep(1)
    print(f'{i + 1}º lugar {v[0]} com {v[1]}')