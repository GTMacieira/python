"""
Split, Join e Enumerate em Python
*Split - divide uma string #str
*Join - Juntar uma lista #str
*Enumerate - Enumerar elementos da liosta #list
"""

lista = [
    [1,2],
    [3,4],
    [5,6]
]

n1,n2,n3 = lista

print (n2)

for v in lista:
    print(v[0], v[1])



# texto = "Você tem brio? Ou você tosquinho?"
# lista_1= texto.split(' ')
#
# for indice, valor in enumerate(lista_1):
#     print(indice, valor, lista_1[indice])




# lista_2= texto.split('?')
# texto_2 = ','.join(lista_1)

# print(texto)
# print(lista_1)
# print(texto_2)


# contagem = 0
# palavra = ''

# for valor in lista_2:
#     print(valor.strip().capitalize())

# for valor in lista_1:
#     qtd_vezes = lista_1.count(valor)
#     if qtd_vezes > contagem:
#         contagem = qtd_vezes
#         palavra = valor
# print(f'A palavra que apareceu mais vezes é {palavra} ({contagem}x)')
#     # print(f'A palavre {valor} apareceu {lista_1.count(valor)}x na frase')
