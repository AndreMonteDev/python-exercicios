# informa media de idade, o nome e idade do homem mais velho e quantas mulheres tem menos de 20 anos

maior_idade = 0
mais_velho = ''
mulheres_menores = 0
idade = 0
soma = 0
for i in range(1, 5):
    print(f'==== {i}a PESSOA ====')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ')
    soma += idade
    if sexo == 'm' and idade > maior_idade:
        maior_idade = idade
        mais_velho = nome
    if sexo == 'f' and idade < 20:
        mulheres_menores += 1
media = soma / 4
print(f'A média de idade do grupo é {media} anos')
print(f'O homem mais velho tem {maior_idade} anos e se chama {mais_velho}')
print(f'Ao todo são {mulheres_menores} com menos de 20 anos')