import math

x = float(input('Digite o angulo qualquer: '))

radianos = math.radians(x)
seno = math.sin(radianos)
coseno = math.cos(radianos)
tangente = math.tan(radianos)

print(f'O seno do ângulo {x}º é {seno:.2f}')
print(f'O coseno do ângulo {x}º é {coseno:.2f}')
print(f'A tangente do ângulo {x}º é {tangente:.2f}')
