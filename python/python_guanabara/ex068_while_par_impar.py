# jogo par impar

import random
vitorias = 0

print('=-'* 9)
print('JOGO PAR OU ÍMPAR')
print('=-'* 9)

while True:
    cpu = random.randint(0, 5)
    jogador_n = int(input('Digite um número: '))
    jogador_p_i = input('Par ou Ímpar [p / i]? ')
    impar = (cpu + jogador_n) % 2
    if impar == 1 and jogador_p_i == 'i':
        print(f'cpu {cpu} x {jogador_n} jogador. Você Venceu!')
        vitorias += 1
    elif impar == 0 and jogador_p_i == 'p':
        print(f'cpu {cpu} x {jogador_n} jogador. Você Venceu!')
        vitorias += 1
    else:
        print(f'cpu {cpu} x {jogador_n} jogador. Você Perdeu!')
        break
print(f'Você venceu {vitorias} vezes!!')

    

