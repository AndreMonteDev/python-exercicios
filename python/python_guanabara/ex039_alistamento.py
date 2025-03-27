from datetime import datetime

ano_atual = datetime.now().year
data_nascimento = int(input('Digite seu ano de nascimento: '))
idade = ano_atual - data_nascimento

if idade == 18:
    print('Está na hora de se alistar Gafanhoto!')
elif idade > 18:
    print(f'Já passou da hora de se alistar Gafanhoto! Você deveria ter se alistado a {idade - 18} anos atrás')
else:
    print(f'Você ainda não precisa se alistar gafanhoto. Só precisará se alistar daqui a {18 -idade} anos')
