nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
letra = input('Digite uma letra ou string: ')
if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    if ' ' in nome:
        print('Seu nome contem espaços')
    else:
        print('Seu nome não contém espaços')
    if letra in nome:
        print(f'{letra} está no nome')
        print(f'A letra ou string {letra} está na posição {nome.index(letra)}')
    else:
        print(f'{letra} não está no nome')   
    print(f'{nome} tem {len(nome)} caracteres')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')
    if int(idade) >= 18:
        print(f'{nome} você já pode ir para o puteiro!')
    else:
        print(f'{nome} você ainda não pode ir para o puteiro!')
else:
    print('Desculpe, você deixou campos vazios.')