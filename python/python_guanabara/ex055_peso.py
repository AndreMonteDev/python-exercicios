maior = float(0)
menor = float(0)

for i in range(5):
    peso = float(input('Digite seu peso: '))
    if i == 0:
        maior = peso
        menor = peso
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso

print(f'maior: {maior:.2f}')
print(f'menor: {menor:.2f}')