km = float(input('Quantos km rodou? '))
dias = float(input('Utilizou o carro por quantos dias? '))

valor = (60 * dias) + (0.15 * km)

print(f'O valor a pagar pelo aluguel do carro é R${valor:.2f}')