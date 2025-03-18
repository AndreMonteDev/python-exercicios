cidade = 'Santo André'
cidadeMaiusculo = cidade.upper()
cidadePnome = cidadeMaiusculo.split()[0]
if cidadePnome == 'SANTO':
    print('A cidade começa com Santo!')
else:
    print('A cidade não começa com Santo!')
