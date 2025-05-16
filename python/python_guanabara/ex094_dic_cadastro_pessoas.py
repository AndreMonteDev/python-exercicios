cadastro = []
pessoas = {}
mulheres = []
soma_idade = 0
while True:
    pessoas['nome'] = str(input('Nome: '))
    pessoas['sexo'] = str(input('Sexo: [M/F] '))
    pessoas['idade'] = int(input('Idade: '))
    cadastro.append(pessoas.copy())
    continuar = str(input('Quer continuar? [S/N] '))
    if continuar in 'Nn':
        break

for pessoa in cadastro:
    soma_idade += pessoa['idade']
    if pessoa['sexo'] in 'Ff':
        mulheres.append(pessoa['nome'])
idade_media = soma_idade / len(cadastro)

print('-=' * 40)
print(cadastro)
print(f'- O grupo tem {len(cadastro)} pessoas.')
print(f'- A média de idade é de {idade_media:.1f} anos.')
print('- As mulheres cadastradas foram: ', mulheres)
print('- Lista das pessoas que estão acima da média: ')

for pessoa in cadastro:
    if pessoa['idade'] > idade_media:
        print(f'{pessoa.keys()} = {pessoa.values()}')