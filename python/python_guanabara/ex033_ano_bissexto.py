ano = int(input('Informe um ano: '))

no_bissexto = ano % 4

if no_bissexto:
    print(f'O ano de {ano} não é bissexto')
else:
    print(f'O ano de {ano} é bissexto')