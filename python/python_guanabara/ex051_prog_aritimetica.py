#exibe a progressão aritimetica dos primeiros 10 números

termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

for n in range(10):
    print(termo, end=' -> ')
    termo += razao

