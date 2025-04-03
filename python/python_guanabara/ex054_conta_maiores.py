from datetime import datetime

ano_atual = datetime.now().year
nascimento = [0] * 7
i = 0
maiores = 0
menores = 0
for i in range(7):
    nascimento[i] = int(input('Digite sua data de nascimento: '))
    if ano_atual - nascimento[i] < 18:
        menores += 1
    else:
        maiores += 1

for i in range(7):
    print(nascimento[i], end=' - ')
print('')
print(f'Ao todo {maiores} pessoas são maiores,')
print(f'E {menores} pessoas são menores')

 