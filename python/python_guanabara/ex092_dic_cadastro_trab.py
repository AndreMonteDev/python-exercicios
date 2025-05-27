# cadastra nome, ano de nascimento, ctps e etc... e informa dados e idade para se aposentar

import datetime

ano_atual = datetime.datetime.now().year
cadastro = {}

cadastro['nome'] = str(input('Nome: '))
ano_nasc = int(input('Ano de Nascimento: '))
idade = ano_atual - ano_nasc
cadastro['idade'] = idade
cadastro['ctps'] = int(input('Nº da CTPS (0 se não tiver): '))
if cadastro['ctps'] != 0:
    cadastro['contratacao'] = int(input('Ano de contratação: '))
    cadastro['salario'] = float(input('Salário: '))
    contribuicao = ano_atual - cadastro['contratacao']
    anos_rest = 35 - contribuicao
    idade_ap = idade + anos_rest
    cadastro['aposentadoria'] = idade_ap
print('=' * 30)
print(cadastro)
print('=' * 30)
for k, v in cadastro.items():
    print(f'O valor de {k} é {v}')