valor_casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o seu salário: '))
anos = int(input('Digite em quantos anos irá pagar: '))
n_parcelas = anos * 12
valor_parcela = valor_casa / n_parcelas

if valor_parcela > (salario * 0.3):
    print(f'Infelizmente o empréstimo foi negado pois a parcela ({valor_parcela:.2f}) utrapassou 30% do seu salário ({salario * 0.3:.2f})')
else:
    print(f'O empréstimo foi aprovado em {n_parcelas} parcelas de R$ {valor_parcela:.2f}.')