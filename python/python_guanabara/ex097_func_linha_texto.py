# Função que escreve texto com traços acompanhando o tamanho do texto
def escreva(txt):
    print('-' * len(txt))
    print(txt)
    print('-' * len(txt))

escreva('Curso de Python')
escreva('do professor')
escreva('Guanabara')