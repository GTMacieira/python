"""
Formatando valores com modificadores

:s - Texto (string)
:d - Inteiro (int)
:f - Número de ponto flutuante (float)
:. (NÚMERO)f - Quantidade de cada decimais (float)
:(CRACTERE) (> ou < ou ^)(QUANTIDADE( (TIPO - d, d ou f)

> - Esquerda
< - Direira
^- Centro
"""

num_1 = 10
num_2 = 3
divisao = num_1/num_2
print(f'{divisao:.2f}') #arrredondar com duas casas decimais
print(f'{divisao:0<100}') #preenche com zeros a esquerda
print(f'{divisao:0^100}') #cantraliza o valor
print(f'{divisao:0>100}') #preenche com zeros a esquerda
# Ao adicionar a mesma quantidade que o número ou string a ser printado os complementos nbão são exibidos

nome = 'guilherme macieira'
print(nome.upper()) #Tudo maiusculo
print(nome.lower()) #Tudo minuculo
print(nome.title()) #Primiras letras maiusculas




