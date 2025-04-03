# Calcula a soma de todos NUMERO IMPARES que são MULTIPLOS DE 3 entre 1 e 500

soma = 0
for n in range(1, 501, 2):
    if (n % 3) == 0:
        soma += n
print(soma)