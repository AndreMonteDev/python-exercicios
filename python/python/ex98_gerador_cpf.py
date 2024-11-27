import random

cpf_quantidade = input('Quantos cpfs tú quer mermão? ')

for quantidade in range(int(cpf_quantidade)):
    cpf_aleatorio = ''

    for numero in range(9):
        numero_aleatorio = random.randint(0, 9)
        cpf_aleatorio += str(numero_aleatorio)
        
    cpf1 = cpf_aleatorio
    i_reg = 10
    resultado_dig1 = 0

    for numero1 in cpf1:
        resultado_dig1 += i_reg * int(numero1)    
        i_reg -= 1

    digito_1 = ((resultado_dig1 * 10) % 11)
    digito_1 = digito_1 if digito_1 <= 9 else 0

    cpf_dig1 = str(cpf1) + str(digito_1)

    j_reg = 11
    resultado_dig2 = 0

    for numero2 in cpf_dig1:
        resultado_dig2 += j_reg * int(numero2)    
        j_reg -= 1

    digito_2 = ((resultado_dig2 * 10) % 11)
    digito_2 = digito_2 if digito_2 <= 9 else 0


    cpf_completo = str(cpf_dig1) + str(digito_2)

    digito_completo = str(digito_1) + str(digito_2)

    print(cpf_completo)

print('Bom Golpe!')