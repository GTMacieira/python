"""
While(enquanto) em Python
utilizado pra realizar ações enquanto
uma condição for verdadeira
"""

i=0
while i<=100:
    if i%2>0:
        i+=1
        #continue #Pula pra o proximo loop
        break #Sai do loop
    print(i)
    i=i+1
print(f'Acabou em {i}')
