# identifica se um número é primo ou não
import math

n = int(input('Digite um número: '))
div_total = 0
for i in range(1, n + 1):
    if n % i == 0:
        div_total += 1
        print(f'\033[33m', end=' ')
    else:
        print(f'\033[31m', end=' ')
    print(f'{i}', end='')
print('')
print(f'O número {n} foi divisivel {div_total} vezes')
if div_total <= 2:
    print('portanto ele é um número primo')
else:
    print('portanto ele não é um número primo')