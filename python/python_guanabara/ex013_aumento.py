def calc_aumento(n, a):
    return n + (n * a)

salario = float(input('Digite o seu salário: '))
aumento = float(input('Digite o aumento em %: '))
aumento_percent = aumento * 0.01

print(f'Seu salario de R$ {salario} com aumento de R$ {aumento} é {calc_aumento(salario, aumento_percent):.2f}')

