i = 0
termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

while i < 10:
    print(termo, end=' -> ')
    termo += razao
    i += 1
print('FIM')