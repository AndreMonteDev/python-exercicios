# Verifica se a frase é um palindromo

frase = input('Digite uma frase: ')
frase_maiuscula = frase.upper().strip()
palavras = frase_maiuscula.split()
frase_sem_espacos = ''.join(palavras)
frase_invertida = ''

for letra in range(len(frase_sem_espacos) -1, -1, -1):
    frase_invertida += frase_sem_espacos[letra]

if frase_sem_espacos == frase_invertida:
    print(f'A frase {frase} é um palíndromo!')
else:
    print(f'A frase {frase} não é um palíndromo!')
# print(frase_maiuscula)
# print(palavras)
print(frase_sem_espacos)
print(frase_invertida)


