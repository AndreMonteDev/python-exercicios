# tabuada
i = 1
while True:
    numero = int(input('Digite um número [-n sair]: '))
    for i in range(1, 11):
        print(f'{numero} X {i:2} = {numero * i}')
    if numero < 0:
        break
