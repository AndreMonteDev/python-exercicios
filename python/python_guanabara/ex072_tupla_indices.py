# buscar item pelo indice em tupla
indice = 0
numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenovo', 'vinte')

indice = int(input('Digite um número entre 0 e 20: '))
while indice not in range(0, 21):
    indice = int(input('Número inválido, por favor digite um número entre 0 e 20: '))

print(f'Você digitou o número {numeros[indice]}')