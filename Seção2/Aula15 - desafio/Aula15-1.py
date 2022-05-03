"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou impar. Caso o usuário não digite um numero inteiro,
informe que nãio eé um número inteiro.
"""

num1 = input('Digite um número inteiro: ')

if num1.isnumeric():
    num1 = int(num1)
    if num1%2 >0:
        print(f'{num1} é ímpar')
    elif num1%2 ==0:
        print(f'{num1} é par')
    else:
        print('Digite um número inteiro')
