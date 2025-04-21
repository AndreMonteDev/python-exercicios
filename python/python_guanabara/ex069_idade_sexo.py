# estatisticas idade e sexo
maiores = 0
homens = 0
mulheres_menores = 0

while True:
    idade = int(input('Digite a idade: '))
    sexo = input('Digite o sexo [m/f]: ').lower()
    if idade > 18:
        maiores += 1
    if sexo == 'm':
        homens += 1
    if sexo == 'f' and idade < 20:
        mulheres_menores += 1
    continuar = input('Quer continuar [s/n]? ').lower()
    if continuar == 'n':
         break
    
print(f'Pessoas com mais de 18 anos: {maiores}')
print(f'Homens cadastrados: {homens}')
print(f'Mulheres com menos de 20 anos: {mulheres_menores}')
