
# def multiplica(*args):
#     multiplicacao_resultado = 1
#     for numero in args:
#         multiplicacao_resultado *= numero
#     return multiplicacao_resultado

# resultado = multiplica(2, 2, 3, 10)

# print(resultado)

def par_impar(x):
    par_impar_resultado = (x % 2)
    if par_impar_resultado == 0:
        return('par')
    else:
        return('impar')

print(par_impar(2))
print(par_impar(1))
print(par_impar(9))
print(par_impar(10))