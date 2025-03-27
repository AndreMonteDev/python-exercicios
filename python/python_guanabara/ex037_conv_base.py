from rich import print

numero = int(input('Entre com um número: '))
opcao = int(input('Escolha uma opção de conversão (1) para binario, (2) para octal e (3) para hexadecimal: '))

if opcao == 1:
    print(f'{numero} em binário {bin(numero)}')
elif opcao == 2:
    print(f'{numero} em octal {oct(numero)}')
elif opcao == 3:
    print(f'{numero} em hexadecimal {hex(numero)}')
else:
    print('Opção inválida')
    
    