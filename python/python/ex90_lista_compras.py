lista_de_compras = []
opcao = ''
i = 0

while opcao != 's':
    print('Selecione uma opção')      
    opcao = input('[i]nserir [a]pagar [l]istar [s]air:')
    if opcao == 'i':
        inserir = input('Digite um intem: ')
        lista_de_compras.append(inserir)
    if opcao == 'l':
        for indice, item in enumerate(lista_de_compras):
            print(indice, item)

print(lista_de_compras)
print(enumerate(lista_de_compras))