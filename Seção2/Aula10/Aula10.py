"""
Operadores relacionais
== > >= < <= !=
"""
num = input('Digite um número: ')


if int(num)%2 == 0:
    print('O número digitado é PAR')
elif int(num)%2 > 0:
    print('O número digitado é IMPAR')
else:
    print(f'{num} não é um número')
