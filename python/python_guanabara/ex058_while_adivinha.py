# jogo que a pessoa tem que adivinhar o número
import random
n = 0
numeroSorteado = random.randint(1, 10)
tentativas = 0

while n != numeroSorteado:
    n = int(input('Digite um número de 1 a 10: '))
    tentativas += 1
    if n == numeroSorteado:
        print('Acertou miseravi!')
    else:
        print('Errou miseravi!')
print('Número de tentativas: ',tentativas)