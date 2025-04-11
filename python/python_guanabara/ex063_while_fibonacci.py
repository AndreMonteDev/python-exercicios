# fibonacci
print('Sequência de Fibonacci')
print('=' * 22)

termos = int(input('Quantos termos você quer exibir? '))

print('-' * 30)
i = 0
t1 = 0
t2 = 1
t3 = 0
print(f'{t1} -> {t2} -> ', end='')

while i < termos - 2:
    t3 = t1 + t2
    print(f'{t3}', end=' -> ')
    i += 1
    t1 = t2
    t2 = t3
print('FIM')
    
   