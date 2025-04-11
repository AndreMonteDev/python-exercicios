# mostra média de valores e qual menor e maior\

n = 0
i = 0
maior = 0
menor = 0
continuar = ''
nao = ('n', 'N')
soma = 0
while continuar not in nao:
    n = int(input('Digite um número: '))
    soma += n
    if menor == 0:
        menor = n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    i += 1
    continuar = input('Quer continuar [n/s]?')
print('-' * 20)
print(f'Você digitou {i} números')
print(f'A média dos números é {(soma / i):.2f}')
print('O maior número é: ', maior)
print('O menor número é: ', menor)

 