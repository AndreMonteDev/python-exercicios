# analisa se a expressão aritimética é válida verificando os parênteses
valido = None
expressao = input('Digite a expressão: ')
pilha = []
for i in expressao:
    if i == '(':
        pilha.append('(')
    elif i == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
   

if len(pilha) == 0:
    print('Expressão aritimética válida!')
else:
    print('Expressão aritimética inválida!')