from rich import print, inspect

lista = list(range(1, 6))
dicionario = {'Nome': 'André', 'Idade': '45'}
nome = 'Meu nome é [reverse][green][b]André[/b][/green][/reverse]'
frase = '[red on yellow b reverse]O Debian 11 (Bullseye) não vem com uma "loja de aplicativos" gráfica como o Ubuntu Software Center por padrão. No entanto, ele possui algumas opções para instalar programas de forma gráfica, dependendo do ambiente de desktop que você está usando.[/]'
print(lista)
print(dicionario)
print(nome)
print(frase)
## inspect(lista)