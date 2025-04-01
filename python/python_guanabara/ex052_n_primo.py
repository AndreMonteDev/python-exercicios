# identifica se um número é primo ou não
import math

n = int(input('Digite um número: '))
primo = False
if n < 2:
    primo = False
else:
    primo = True
for i in range(2, int(math.sqrt(n) + 1)):
    if n % i == 0:
        primo = False
    else:
        primo = True
 

print(f'Número primo? {primo}')
