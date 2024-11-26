
cpf = input('Digite os 9 primeiro dígitos do seu cpf: ')

dig1 = int(cpf[0]) * 10
dig2 = int(cpf[1]) * 9
dig3 = int(cpf[2]) * 8
dig4 = int(cpf[3]) * 7
dig5 = int(cpf[4]) * 6
dig6 = int(cpf[5]) * 5
dig7 = int(cpf[6]) * 4
dig8 = int(cpf[7]) * 3
dig9 = int(cpf[8]) * 2

cpf_soma_multi = (dig1 + dig2 + dig3 + dig4 + dig5 + dig6 + dig7 + dig8 + dig9) * 10

cpf_resto_div_11 = cpf_soma_multi % 11

print(cpf_soma_multi)
print(cpf_resto_div_11)

if cpf_resto_div_11 > 9:
    digito_1 = 0
else:
    digito_1 = cpf_resto_div_11

print(f'O primeiro digito do cpf é {digito_1}')

print(dig1, dig2, dig3, dig4, dig5, dig6, dig7, dig8,  dig9)