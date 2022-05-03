"""
Listas
Fatiamento
Appent, insert, pop, del, clear, extend, +, min, max
range
"""

# lista = ['A', 'B', 'C', 'D', 'E']
#
# print(lista[1])
# print(lista)
# lista[-1] = 'teste'
#
# print(lista)
# print(lista[0:3]) #Fatiamento/Excluso o ultimo item

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = list(range(1,10))
# l2 = [4, 5, 6]
# l3 = l1 + l2
# l1.extend(l2) #adciona nela mesma o valor desgnado nos parnteses
# l2.append('d') #adiciona no final da lista o valor do parateses
# l2.insert(0,'banana') #Inclui na lista o valor entre parenteses na posição indicada antes da virgula
# l2.pop() #remove o valor da lista de acordo com os parenteses
# del(l1[3:5])#remove o trecho indicado


print(max(l1))
print(min(l1))
print(l2)
# print(l2)
# print(l3)

for valor in l2:
    print(valor)
