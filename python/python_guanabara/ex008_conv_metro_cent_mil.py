
while True:
    numero = input('Digite o tamanho em metros: ')

    try:
        numero = int(numero)
        cm = numero * 100
        mm = cm * 10
        print(f'{numero} metros equivale a {cm} centimetros e {mm} milimetros')
        break
    except ValueError:
        print('Favor digitar um número inteiro')
