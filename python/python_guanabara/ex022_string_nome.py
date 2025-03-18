nomeCompleto = 'André Luiz Monte'

nomeMaiusculo = nomeCompleto.upper()
nomeMinusculo = nomeCompleto.lower()
nomeSemEspacos = ''.join(nomeCompleto.split())
numeroLetrasNome = len(nomeSemEspacos)
primeiroNome = nomeCompleto.split()[0]
numeroLetrasPnome = len(primeiroNome)

print('Nome Completo:',nomeCompleto)
print('Nome com letras maiúsculas:',nomeMaiusculo)
print('Nome com letras minúsculas:',nomeMinusculo)
print(f'{nomeCompleto} tem {numeroLetrasNome} letras')
print(f'O primeiro nome de {nomeCompleto} é {primeiroNome}')
print(f'O nome {primeiroNome} tem {numeroLetrasPnome} letras')