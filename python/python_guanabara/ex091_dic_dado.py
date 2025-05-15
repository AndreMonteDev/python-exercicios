# sorteia 4 numeros de dado(1 a 6) e ordena por ordem de quem tirou o maior
import time
import random

jogador1 = random.randint(1, 6)
jogador2 = random.randint(1, 6)
jogador3 = random.randint(1, 6)
jogador4 = random.randint(1, 6)

jogo = {'jogador1': jogador1, 'jogador2': jogador2, 'jogador3': jogador3, 'jogador4': jogador4}

print(jogo)

for k, v in jogo.items():
    time.sleep(1)
    print(k, v)