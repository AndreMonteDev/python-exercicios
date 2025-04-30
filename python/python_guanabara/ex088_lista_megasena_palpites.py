import time
from random import randint
palpite = []
palpites = []
print('-' * 36)
print(f'{"JOGOS DA MEGASENA":^36}')
print('-' * 36)

jogos = int(input('Quantos jogos? '))
print(f'{f"--== Sorteando {jogos} jogos ==--":^36}')
for jogo in range(jogos):
    while len(palpite) < 6:
        n = randint(1, 60)
        if not n in palpite:
            palpite.append(n)
    palpites.append(sorted(palpite[:]))
    palpite.clear()

print('-' * 36)

for i, p in enumerate(palpites):
    time.sleep(1)
    print(f'Jogo {i + 1}: {p}')
print(f'{"--== BOA SORTE ==--":^36}')
