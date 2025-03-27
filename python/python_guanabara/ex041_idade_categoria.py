from datetime import datetime

ano_atual = datetime.now().year

data_nascimento = int(input('Digite seu ano de nascimento: '))

idade = ano_atual - data_nascimento

if idade <= 9:
    print(f'Você tem {idade} e sua categoria é MIRIM.')
elif idade > 9 and idade <= 14:
    print(f'Você tem {idade} e sua categoria é INFANTIL.')
elif idade > 14 and idade <= 19:
    print(f'Você tem {idade} e sua categoria é JUNIOR.')
elif idade > 19 and idade <= 20:
    print(f'Você tem {idade} e sua categoria é SENIOR.')
else:
    print(f'Você tem {idade} e sua categoria é MASTER.')
