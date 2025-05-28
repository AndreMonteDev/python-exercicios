# Função que recebe vários números e informa quantos valores e o maior valor
import time

def maior(* lista):
    print('-=' * 30)
    print('Analisando os valores passados...')
    for i in lista:
        time.sleep(1)
        print(i, end=' ')
    print(f'Foram passados {len(lista)} valores ao todo.')
    print(f'O maior valor informado foi {max(lista)}.')

maior(1, 2, 3, 4, 5, 6)
maior(6, 20, 30, 33, 300)
maior(3,4,5,6,7,3,56,776,87,33,45,45,3)