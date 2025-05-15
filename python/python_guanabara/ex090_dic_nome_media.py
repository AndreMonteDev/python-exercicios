# cadastra nome e media e exibe nome media e situação
situacao = ''
nome = str(input('Nome: '))
media = float(input('Média: '))
if media >= 7:
    situacao = 'aprovado'
else:
    situacao = 'reprovado'

aluno = {'nome': nome, 'media': media, 'situacao': situacao}

print('NOME      MÉDIA  SITUAÇÃO')
print(f'{aluno["nome"]:<10}{aluno["media"]:<7.1f}{aluno["situacao"]}')