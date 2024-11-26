

cpf_digitado = '22311972866'
cpf1 = cpf_digitado[:9]
i_reg = 10
resultado_dig1 = 0

for numero1 in cpf1:
    resultado_dig1 += i_reg * int(numero1)    
    i_reg -= 1

digito_1 = ((resultado_dig1 * 10) % 11)
digito_1 = digito_1 if digito_1 <= 9 else 0

print(digito_1)

cpf_dig1 = str(cpf1) + str(digito_1)

print(cpf_dig1)


j_reg = 11
resultado_dig2 = 0

for numero2 in cpf_dig1:
    resultado_dig2 += j_reg * int(numero2)    
    j_reg -= 1

digito_2 = ((resultado_dig2 * 10) % 11)
digito_2 = digito_2 if digito_2 <= 9 else 0

print(digito_2)

cpf_completo = str(cpf_dig1) + str(digito_2)

print(cpf_completo)

print(cpf_completo[9::])

digito_completo = str(digito_1) + str(digito_2)

print(digito_completo)

if cpf_digitado[9::] == digito_completo:
    print('CPF válido')
else:
    print('CPF inválido')