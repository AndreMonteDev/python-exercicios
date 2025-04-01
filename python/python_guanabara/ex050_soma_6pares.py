# Lê 6 número e soma apenas os pares

soma_par = 0

for n in range(6):
    num = int(input('Digite um número: '))
    if (num % 2) == 0:
        soma_par += num

print(f'A soma dos número pares é: {soma_par}')
