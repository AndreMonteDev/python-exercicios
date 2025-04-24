lista = []
numero = 0
while True:
    numero = int(input('Digite um valor: '))
    if numero in lista:
        print('Valor duplicado! Não vou adicionar...')
    else:
        lista.append(numero)
        print('Valor adicionado com sucesso...')
    continuar = input('Deseja continuar? [S/N] ')
    if continuar in 'Nn':
        break

print(f'Você adicionou os valores {sorted(lista)}')
