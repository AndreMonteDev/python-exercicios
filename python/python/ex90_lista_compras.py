lista_de_compras = []
opcao = ''
i = 0

while opcao != 's':

    print('Selecione uma opção')      
    opcao = input('[i]nserir [a]pagar [l]istar [s]air: ')
    
    if opcao == 'i':
        inserir = input('Digite um intem: ')
        lista_de_compras.append(inserir)
    
    elif opcao == 'l':
        for indice, item in enumerate(lista_de_compras):
            print(indice, item)
    
    elif opcao == 'a':
        apagar = input('Digite o número do item para apagar: ')
           
        if int(apagar) > len(lista_de_compras):
            print(f'O número está fora da lista. Digite um número entre 0 e {len(lista_de_compras)}')       

        else:
            del lista_de_compras[int(apagar)]
