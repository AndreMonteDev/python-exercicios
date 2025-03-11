while True:
    numero = input('Digite um número inteiro: ')

    try:
        numero = int(numero)
        for n in range(11):
            print(f'{numero} x {n} = {n * numero}')
        break
    except ValueError:
        print('Favor digitar um número inteiro válido.')
