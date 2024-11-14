palavra_secreta = 'pente'
letra_digitada = ''
letras_acertadas = ''
tentativas = 0

print('Descubra a palavra Secreta.')
print('** Dica 1: Você gosta!')
print('** Dica 2: Começa com P !')
        
while letra_digitada != '.':
   
    letra_digitada = input('Digite uma letra ( . para sair): ')
    tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas 1 letra por favor!')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''

    for letra in palavra_secreta:

        if letra in letras_acertadas:
            palavra_formada += letra
        else:
            palavra_formada += '*'
    
    print(f'Palavra secreta: {palavra_formada}')
    print(f'Tentativas: {tentativas}')

    if palavra_formada == palavra_secreta:
        print('Você ganhou!')
        

