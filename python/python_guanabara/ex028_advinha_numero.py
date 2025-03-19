import random
n = 0
numeroSorteado = random.randint(1, 5)

while n != numeroSorteado:
    n = int(input('Digite um número de 1 a 5: '))
    if n == numeroSorteado:
        print('Acertou miseravi!')
    else:
        print('Errou miseravi!')