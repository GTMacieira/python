""""
Expressões condicionais usando or
"""

from sqlalchemy import false


a = 0
b = None
c = false
d = []
e = {}
f = 22
g = 'Guilherme'

variavel = a or b or c or d or e or f or g

print(variavel)

#nome= input('Qual o seu nome? ')

#print(nome or 'Você não digitou nada')