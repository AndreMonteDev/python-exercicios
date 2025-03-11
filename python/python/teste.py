produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritorio',
}

def lista_dicionario(dicionario):
    for chave, valor in dicionario.items():
        print(chave, valor)
    print()

lista_dicionario(produto) 