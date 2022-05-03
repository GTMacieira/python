"""
For in
Iterando strings com for
Função tange(start=0, stop, step=1)
"""

texto='Guilherme'

# for letra in texto:
#     print(letra)

# for numero in range(5, 10, 1):
#     print(numero)

novo_texto=''
for letra in texto:
    if letra == 'e':
        novo_texto = novo_texto+letra.upper()
    elif letra == 'i':
        novo_texto += letra.upper()
    else:
        novo_texto += letra
print(novo_texto)