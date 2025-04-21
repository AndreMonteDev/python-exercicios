import random


sorteio = (random.randint(1, 10), random.randint(1, 10),random.randint(1, 10),random.randint(1, 10),random.randint(1, 10))

print('Números sorteados:',sorteio)
print('Número menor:', min(sorteio))
print('Número maior:', max(sorteio))

