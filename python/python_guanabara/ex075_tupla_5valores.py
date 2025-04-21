# procurar 9, 3 e numeros pares em tupla

v1 = int(input('Digite um número: '))
v2 = int(input('Digite outro número: '))
v3 = int(input('Digite outro número: '))
v4 = int(input('Digite outro número: '))

tupla = (v1, v2, v3, v4)

print('=' * 30)
print('Você digitou os valores:', tupla)
if 9 in tupla:
    nove = tupla.count(9)
    print(f'O valor 9 apareceu {nove} vezes')
else:
    print('Não tem o valor 9 na tupla')
if 3 in tupla:
    posicao = tupla.index(3)
    print(f'O valor 3 está na posição: {posicao + 1}')
else:
    print('Não tem o valor 3 na tupla')
print('Os valores pares digitados foram: ', end='')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')
  