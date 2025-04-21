# exibe as vogais de cada palavra de uma tupla

tupla = ('abacaxi', 'banana', 'linguiça', 'bolo', 'computador', 'origami', 'salada', 'palhaço', 'cagada', 'cerveja', 'tubaina')

for palavra in tupla:
    print(f'Na palavra {palavra} temos as vogais: ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
    print('')