

opcao = 0
num1 = int(input('Digite um número [n1]: '))
num2 = int(input('Digite outro número [n2]: '))

while opcao != 5:
    print('[1] somar')
    print('[2] multiplicar')
    print('[3] maior')
    print('[4] novos números')
    print('[5] sair')
    opcao = int(input('Digite uma opção: '))
    if opcao == 1:
        print(f'{num1} + {num2} é igual a {num1 + num2}')
    if opcao == 2:
        print(f'A multiplicação de {num1} X {num2} é igual a {num1 * num2} ')
    if opcao == 3:
        if num1 > num2:
            print(f'{num1} é maior que {num2}')
        else:
            print(f'{num2} é maior que {num1}')
    if opcao == 4:
        num1 = int(input('Digite um número [n1]: '))
        num2 = int(input('Digite outro número [n2]: '))

