frase = 'O Python é uma linguagem de programação ' \
    'multiparadigma. ' \
    'Python foi criado por Guido van Rossum.'

i = 0
qtd_letra_atual = 0
qtd_letra_maior = 0
letra_atual = ' '

while i < len(frase):

    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtd_letra_atual = frase.count(letra_atual)

    if qtd_letra_maior < qtd_letra_atual:
        qtd_letra_maior = qtd_letra_atual
        letra_maior = letra_atual

    i += 1

print(f'Letra com maior quantidade: {letra_maior}')
print(f'Quantidade: {qtd_letra_maior}')

        