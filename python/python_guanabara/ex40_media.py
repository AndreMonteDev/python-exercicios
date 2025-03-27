nota1 = float(input('Entre com a primeira nota: '))
nota2 = float(input('Entre com a segunda nota: '))
media = (nota1 + nota2) / 2

if media < 5:
    print(f'Sua media foi {media} e você foi reprovado!')
elif media >= 5 and media < 7:
    print(f'Sua media foi {media} e você está de recuperação!')
else:
    print(f'Sua media foi {media}. Parabés, você foi aprovado!')
