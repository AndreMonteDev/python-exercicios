lista = []

for i in range(5):
    n = int(input('Digite um número: '))
    if not lista:
        lista.append(n)
        print(f'O número {n} foi adicionado na posição 0')
    else:
        for c, v in enumerate(lista):
            if n < v:
                lista.insert(c, n)
                print(f'O valor {n} foi adicionado na posição {c}')
                break
        else:
            lista.append(n)
            print(f'O número {n} foi adicionado na posição {len(lista) + 1}')
                
print(lista)
