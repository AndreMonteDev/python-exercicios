# Função que faz contagens de 1 a 10, de 10 até 0 passo 2 e contagem personalizada
import time

def conta(x, y, z):
    print('-=' * 20)
    print(f'Contagem de {x} até {y} de {z} em {z}:')
    if x > y and z >= 0:
        z = z * -1
        y = y - 1
    if x > y and z == 0:
        z= - 1
        y = y - 1
    if x < y:
        y = y + 1
    if x < y and z == 0:
        z = 1
    for i in range(x, y, z):
        time.sleep(1)
        print(i, end=' ')
    print('FIM')
    print('-=' * 20)


conta(1, 10, 1)
conta(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
x = int(input('Início: '))
y = int(input('Fim: '))
z = int(input('Passo: '))
conta(x, y, z)
