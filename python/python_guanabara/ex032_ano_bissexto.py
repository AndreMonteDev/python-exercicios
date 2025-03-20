ano = int(input('Informe um ano: '))

no_bissexto = ano % 4 and ano % 100 == 0 or ano % 400 != 0

print(no_bissexto)
if no_bissexto:
    print(f'O ano de {ano} não é bissexto')
else:
    print(f'O ano de {ano} é bissexto')