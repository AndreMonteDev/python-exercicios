# insere ano de nascimento e retorna se a pessoa precisa votar ou não

import datetime

ano_nasc = 0
ano_atual = datetime.datetime.now().year
idade = ano_atual - ano_nasc

def voto(ano_nasc):
    idade = ano_atual - ano_nasc
    if (idade >= 16 and idade < 18) or idade >= 65:
        resultado = print(f'Com {idade} anos, o VOTO É OPCIONAL.')
    if idade >= 18 and idade < 65:
        resultado = print(f'Com {idade} anos, o VOTO É OBRIGATÓRIO.')
    if idade < 16:
        resultado = print(f'Com {idade} anos, o VOTO NÃO É PERMITIDO.')
    return resultado

voto(1979)
voto(2018)
voto(2009)
voto(1900)