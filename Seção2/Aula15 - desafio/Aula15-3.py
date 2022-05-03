"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos,
escreva "Seu nome é curto" se tiver 5 ou 6 letras, escreva "Seu nome é normal", maior que 6 letras "Seu nome é muito grande"
"""

nome= input('Escreva seu priemeiro nome: ')

if len(nome)<=4:
    print('Seu nome é curto')
elif len(nome)>4 and len(nome)<=6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')
