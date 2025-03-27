from random import randint


opcoes = {1:'pedra ✊', 2:'papel 🖐️',3:'tesoura ✌️'}
cpu = randint(1, 3)
o = 10

while o != 0:
    cpu = randint(1, 3)
    o = int(input('Digite (1) para pedra ✊, (2) para papel 🖐️ e  (3) para tesoura ✌️ (0)sair: '))
    if o == cpu:
        print(f'Empate! cpu {opcoes[cpu]} X Gafanhoto {opcoes[o]}')
        print('')
    elif (o == 1 and cpu == 3) or (o == 2 and cpu == 1) or (o == 3 and cpu == 2):
        print(f'Ganhou! cpu {opcoes[cpu]} X Gafanhoto {opcoes[o]}')
        print('')
    elif (cpu == 1 and o == 3) or (cpu == 2 and o == 1) or (cpu == 3 and o == 2):
        print(f'Perdeu! cpu {opcoes[cpu]} X Gafanhoto {opcoes[o]}')
        print('')
                  
              

##✌️🖐️✊