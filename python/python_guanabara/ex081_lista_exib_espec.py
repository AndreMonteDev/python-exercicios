# cadastra valores, exibe quantos valores, exibe em ordem decrescente, verifica se há o valor 5
lista = []
while True:
    v = int(input('Digite um valor: '))
    lista.append(v)
    continuar = input('Quer continuar? [S/N] ')
    if continuar in 'Nn':
        break
print('-' * 30)
lista.sort(reverse=True)
print(f'Você digitou {len(lista)} elementos.')
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')