# Cadastro de aluno e notas e exibição de média e boletim

nome = ''
n1 = 0
n2 = 0
notas = []
aluno = []
boletim = []
continuar = ''
mostrar = 0
while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    notas.append(n1)
    notas.append(n2)
    aluno.append(nome)
    aluno.append(notas[:])
    boletim.append(aluno[:])
    notas.clear()
    aluno.clear()
    continuar = str(input('Quer continuar? [S/N]'))
    if continuar in 'nN':
        break
print(boletim)
print('=' * 25)
print(f'{"BOLETIM":^25}')
print('=' * 25)
print(f'{"No.":<4}{"NOME":<12}{"MÉDIA":>9}')
print('-' * 25)
for i, aluno in enumerate(boletim):
    media = (aluno[1][0] + aluno[1][1])/2
    print(f'{i:<4}{aluno[0]:<12}{media:>9.2f}')
print('-' * 25)
while True:
    mostrar = int(input('Mostrar notas de qual aluno? (999 interropmpe): '))
    if mostrar == 999:
        break
    else:
        print(f'As notas de {boletim[mostrar][0]} são {boletim[mostrar][1]}')
