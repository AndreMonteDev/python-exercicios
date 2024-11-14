
hora = input('Digite a hora: ')
hora_int = None

if hora.isdigit():
    hora_int = int(hora)
else:
    print('Você não digitou um número inteiro')

if (hora_int >= 0) and (hora_int <=11):
    print('Bom dia')
elif (hora_int >= 12) and (hora_int <=17):
    print('Boa tarde')
elif (hora_int >= 18) and (hora_int <=23):
    print('Boa noite')
else:
    print('Você não digitou uma hora válida de 0 a 23')