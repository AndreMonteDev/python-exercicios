altura = 0
largura = 0
m2 = 0
litros = 0

while True:
    try:
        largura = float(input('Digite a largura da parede em metros: '))
    except ValueError:
        print('Favor digitar um valar válido')

    try:
        altura = float(input('Digite a largura da parede em metros: '))
    except ValueError:
        print('Favor digitar um valar válido')

    m2 = largura * altura
    litros = m2 / 2
    print(f'Você precisa de {litros} litros para pintar uma parede de {m2} metros quadrados')
    break