import math

cat_op = float(input('Informe o comprimento do cateto oposto de um triângulo:'))
cat_adj = float(input('Informe o comprimento do cateto adj de um triângulo:'))

hypot = math.hypot(cat_op, cat_adj)

print(f'A hypotenusa do triangulo é: {hypot:.2f}')