distancia = int(input('Digite a distância da viagem em Km: '))

if distancia > 200:
    passagem = distancia * 0.45
else:
    passagem = distancia * 0.50

print(f'O valor da passagem é de {passagem} reais')