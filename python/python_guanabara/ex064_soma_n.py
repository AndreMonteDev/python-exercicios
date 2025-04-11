# soma número e sai ao digitar 999
soma = 0
n = 0
cont = 0
while n != 999:
    n = int(input('Digite um número [999 sair]: '))
    if n != 999:
        soma += n
    cont += 1
print(f'Você digitou {cont - 1} números')
print(f'A soma do número é {soma}')