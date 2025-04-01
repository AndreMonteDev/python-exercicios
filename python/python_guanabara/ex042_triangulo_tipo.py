r1 = int(input('Informe o valor de uma reta r1: '))
r2 = int(input('Informe o valor de outra reta r2: '))
r3 = int(input('Informe o valor de uma reta r3: '))

if r1 + r2 <= r3 or r1 + r3 <= r2 or r2 + r3 <= r1:
    print('Não é possível formar um triângulo')
elif r1 == r2 and r2 == r3:
    print('Triangulo Equilátero.')
elif (r1 == r2 and r1 != r3) or (r1 == r3 and r3 != r2) or(r2 == r3 and r3 != r1):
    print('Triangulo Isósceles.')
elif r1 != r2 and r2 != r3:
    print('Triangulo Escaleno')
    