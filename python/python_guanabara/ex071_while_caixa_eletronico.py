# Caixa Eletronico

print('=' * 20)
print(('Banco Fish').center(20))
print('=' * 20)

while True:
    valor = int(input('Qual o valor que deseja sacar? R$ '))
    resto = valor
    if resto >= 50:
        cinquenta = resto // 50
        resto = resto % 50
        print(f'Total de {cinquenta} cédulas de R$ 50')
    if resto >=20 and resto < 50:
        vinte = resto // 20
        resto = resto % 20
        print(f'Total de {vinte} cédulas de R$ 20')
    if resto >=10 and resto < 20:
        dez = resto // 10
        resto = resto % 10
        print(f'Total de {dez} cédulas de R$ 10')    
    if resto >=5 and resto < 10:
        cinco = resto // 5
        resto = resto % 5
        print(f'Total de {cinco} cédulas de R$ 5')    
    if resto >=1 and resto < 5:
        um = resto // 1
        resto = resto % 1
        print(f'Total de {um} cédulas de R$ 1')
    else:
        break