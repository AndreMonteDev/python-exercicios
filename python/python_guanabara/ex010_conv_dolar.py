dolar = 5.90

while True:
    numero = input('Digite um valor: ')

    try:
        numero = float(numero)
        print(f'{numero} reais equivale a {numero} = {numero / dolar} dolares')
        break
    except ValueError:
        print('Favor digitar um número inteiro válido.')
