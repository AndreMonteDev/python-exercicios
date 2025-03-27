valor = float(input('Digite o preço: '))
opcao = int(input('Digite uma opção de pagamento (1) para à vista, (2) para à vista no cartão, (3) para 2x no cartão e (4) para 3x no cartão: '))

if opcao == 1:
    preco = valor * 0.9
elif opcao == 2:
    preco = valor * 0.95
elif opcao == 3:
    preco = valor 
elif opcao == 4:
    preco = valor * 1.2
else:
    print('Escolha um valor válido por favor.')

print(f'O valor de R$ {valor:.2f} ficou em R$ {preco:.2f}')