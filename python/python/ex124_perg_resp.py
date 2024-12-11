# Exercicio 124 Jogo de Perguntas e Respostas

perguntas = [
    {
        'Pergunta': 'Quanto é 2 + 2 ?',
        'Opcoes': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5 * 5 ?',
        'Opcoes': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10 / 2 ?',
        'Opcoes' : ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]


for pergunta in perguntas:
    print(f'')
    print(pergunta['Pergunta'])
    print(f'')
    print('Opções:')
    
    indice = 0
    for opcao in pergunta['Opcoes']:
        print(f'{indice}) {opcao}')
        indice += 1

    opcao_digitada = input('Escolha uma opção: ')

    opcao_escolhida = pergunta['Opcoes'][int(opcao_digitada)]

    print(opcao_escolhida)