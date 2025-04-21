# exibe as vogais de cada palavra de uma tupla

tupla = ('abacaxi', 'banana', 'linguiça', 'bolo', 'computador', 'origami', 'salada', 'palhaço', 'cagada', 'cerveja', 'tubaina')

for palavra in range(0, len(tupla)):
    print(f'Na palavra {(tupla[palavra]).upper()} temos as vogais: ', end='')
    for letra in range(0, len(tupla[palavra])):
        if tupla[palavra][letra] in 'aeiou':
            print(tupla[palavra][letra], end=' ')
    print('')

# ou

# tupla = ('abacaxi', 'banana', 'linguiça', 'bolo', 'computador', 'origami', 'salada', 'palhaço', 'cagada', 'cerveja', 'tubaina')

# for palavra in tupla:
#     print(f'Na palavra {palavra.upper()} temos as vogais: ', end='')
#     for letra in palavra:
#         if letra.lower() in 'aeiou':
#             print(letra, end=' ')
#     print('')