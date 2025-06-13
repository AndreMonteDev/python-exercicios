# função que recebe um valor e retorna o fatorial

def fatorial(n):
    r = 1
    for i in range(1, n + 1):
        r *= i
    return r

print(fatorial(9))