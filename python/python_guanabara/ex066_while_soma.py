# soma números e sai com 999
numero = 0
soma = 0
qtd = 0
while True:
    numero = int(input('Digite um número [999 sair]: '))
    if numero == 999:
        break
    soma += numero
    qtd += 1
print(f'Foram digitados {qtd} números e a soma deles é {soma}')