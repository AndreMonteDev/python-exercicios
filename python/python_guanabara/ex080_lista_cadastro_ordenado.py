# insere 5 valores em uma lista na ordem correta

lista = []

for i in range(5):
    n = int(input('Digite um valor: '))
    if not lista or n > lista[-1]:
        lista.append(n)
        print(f'O valor foi inserido na posição {len(lista) - 1} da lista')
        print('-=' * 30)
    else:
        for i, valor in enumerate(lista):
            if n <= valor:
                lista.insert(i, n)
                print(f'O valor foi inserido na posição {i} da lista')
                print('-=' * 30)

                break

print(lista)