"""
Manipulando strings
*String incices
*Fatiamenro de Strings [inicio:fim:passo]
*Funções bilt-in len, abs, type, print, etc
"""

#incice
# Positivos
text= 'Guilherme Talpo Macieira'
print(text[8])#tras o caracter desejado
#negativos
print(text[-1])#trás o ultimo caracter
#Fatiamento
text_fat = text[0:15] # pegará do caracter 0 ao 14, pois exclui o ultimo caracter, ao omitir o numero entes ou depois dos dois pontos, considerará a partir do zero e até o ultimo caracter
text_fat2 = text[0::2] # Atribui um passo pra pegar os cracteres
print(text_fat)
print(text_fat2)

#Função Len

print(len(text))