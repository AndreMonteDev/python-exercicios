def multiplica(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = multiplica(2)
triplicar = multiplica(3)
quadriplicar = multiplica(4)

print(duplicar(5))
print(triplicar(5))
print(quadriplicar(5))