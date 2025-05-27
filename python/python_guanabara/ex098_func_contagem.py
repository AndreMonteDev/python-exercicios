# Função que faz contagens de 1 a 10, de 10 até 0 passo 2 e contagem personalizada
import time

def conta10():
    print('-=' * 20)
    print('Contagem de 1 até 10 de 1 em 1:')
    for i in range(1, 11):
        time.sleep(1)
        print(i, end=' ')
    print('FIM')
    print('-=' * 20)

def conta_menos10():
    print('-=' * 20)
    print('Contagem de 10 até 0 de 2 em 2:')
    for i in range(10, -1, -2):
        time.sleep(1)
        print(i, end=' ')
    print('FIM')
    print('-=' * 20)

def conta_personal(x, y, z):
    print('-=' * 20)
    if x > y and z > 0:
        z = z * -1
    if x > y:
        y = y - 1
    if x < y:
        y = y + 1
    if x > y and z == 0:
        z = -1
    if x < y and z == 0:
        z = 1
    print(f'Contagem de {x} até {y} de {z} em {z}:')
    for i in range(x, y, z):
        time.sleep(1)
        print(i, end=' ')
    print('FIM')
    print('-=' * 20)

print('Agora é sua vez de personalizar a contagem!')
x = int(input('Início: '))
y = int(input('Fim: '))
z = int(input('Passo: '))
conta_personal(x, y, z)