# Função que calcula uma área
def area(l, c):
    a = l * c
    print(f'A área de um terrano de {l:.2f} x {c:.2f} metros é de {a:.2f}m2')

print('Controle de Terrenos')
print('--------------------')
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(largura, comprimento)