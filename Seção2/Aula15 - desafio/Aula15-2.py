"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada.
Ex. Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23
"""

hora =  input('Que horas são? ')

if hora.isnumeric():
    hora=int(hora)
    if hora >= 0 or hora <= 23:
        if hora<=11:
            print('Bom dia!')
        elif hora>11 and hora<=17:
            print('Boa tarde!')
        else:
            print('Boa noite!')
