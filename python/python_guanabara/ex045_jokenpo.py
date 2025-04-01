from random import randint
from time import sleep
import os
# print('**** JOGO DE JO KEN PO ****')
# print('-= Opções =-')
# print('[1] pedra ✊')
# print('[2] papel 🖐️')
# print('[3] tesoura ✌️')
opcoes = {1:'pedra ✊', 2:'papel 🖐️',3:'tesoura ✌️'}
cpu = randint(1, 3)
o = 10

while o != 0:
    input('Pressione qualquer tecla para continuar...')
    os.system('cls')
    print('**** JOGO DE JO KEN PO ****')
    print('-= Opções =-')
    print('[1] pedra ✊')
    print('[2] papel 🖐️')
    print('[3] tesoura ✌️')
    cpu = randint(1, 3)
    o = int(input('Digite uma opção (0)sair: '))
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO')
    sleep(1)
    if o == cpu:
        print(f'Empate! cpu {opcoes[cpu]} X  {opcoes[o]} Gafanhoto')
        print('')
    elif (o == 1 and cpu == 3) or (o == 2 and cpu == 1) or (o == 3 and cpu == 2):
        print(f'Ganhou! cpu {opcoes[cpu]} X {opcoes[o]}  Gafanhoto')
        print('')
    elif (cpu == 1 and o == 3) or (cpu == 2 and o == 1) or (cpu == 3 and o == 2):
        print(f'Perdeu! cpu {opcoes[cpu]}  X  {opcoes[o]} Gafanhoto')
        print('')
                  
              

##✌️🖐️✊