salario = float(input('Informe seu salário em reais: '))

if salario > 1250:
    aumento = salario * 0.1
else:
    aumento = salario * 0.15

print(f'O aumento de salário referente a R${salario} é de R${aumento}, totalizando R${salario + aumento}')