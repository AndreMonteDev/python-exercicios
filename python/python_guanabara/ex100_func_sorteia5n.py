# Função que sorteia 5 números, insere em uma lista e soma apenas os números pares
import time
import random

numeros = []

def sorteia():
    print('Sorteando 5 valores da lista: ', end=' ')
    for i in range(5):
        time.sleep(1)
        x = random.randint(1, 10)
        numeros.append(x)
        print(x, end=' ')
    print('PRONTO!')

def soma_pares():
    soma = 0
    for numero in numeros:
        if numero % 2 == 0:
            soma += numero
    print(f'Somando os valores pares de {numeros}, temos {soma}')


sorteia()
soma_pares()