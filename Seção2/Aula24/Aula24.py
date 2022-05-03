"""
For/Else em python
"""

variavel = ['Guilherme', 'João', 'Maria']

comec_com_j=False

for valor in variavel:
    if valor.lower().startswith('j'):
        print(valor)
        break
else:
    print('Não existe palavra que começa com J.')






# for valor in variavel:
#     if valor.lower().startswith('j'):
#         comec_com_j = True
#
# if comec_com_j:
#     print('Existe uma palavra que começa com J.')
# else:
#     print('Não existe uma palavra que começa com J.')

# for valor in variavel:
#     if valor.startswith('J'):
#         print('Começa com J ', valor)
#     else:
#         print('Não começa com J ', valor)

#     continue / break
