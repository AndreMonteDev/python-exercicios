#exibe a progressão aritimetica dos primeiros 10 números

termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
i = 0
total = 0
mais = 10
# for n in range(10):

while mais != 0:
    total = total + mais
    while i < total:
        print(termo, end=' -> ')
        termo += razao
        i += 1
    print('PAUSA')
    mais = int(input('Deseja exibir mais quantos termos? '))
print(f'Foram exibidos no total {total} termos')