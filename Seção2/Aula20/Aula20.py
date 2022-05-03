"""
While /  Else
Contadores
Acumuladores
"""

# contador =0
#
# # contador
# while contador <= 10:
#     print(contador)
#     contador+=1

# Acumulador
contador =1
acumulador = 1

while contador <= 10:
    print(contador, acumulador)

    acumulador=acumulador+contador
    contador+=1
else:
    print(f'O contador chegou em {contador}')
