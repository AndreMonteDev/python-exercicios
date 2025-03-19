velocidade = int(input('Qual a velocidade em km/h ao passar no radar: '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'Você foi multado em R${multa}.')
else:
    print(f'Você não foi multado')