numero = input('Digite um número: ')
resto_da_divisao_numero = int(numero) % 2
print (f'O resto da divisão é: {resto_da_divisao_numero}')
if resto_da_divisao_numero:
    print ('O número é ímpar')
else:
    print ('O número é par')
