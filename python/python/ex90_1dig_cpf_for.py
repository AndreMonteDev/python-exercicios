
cpf = '376960550'
num = []
i = 10
i_cres = 0
soma = 0

for numero in cpf:
    num.append(i * int(numero))
    soma += num[i_cres]
    i -= 1
    i_cres += 1
    
resto = ((soma * 10) % 11)

if resto >= 9:
    digito = 0
else:
    digito = resto

print(num)
print(soma)
print(resto)
print(digito)