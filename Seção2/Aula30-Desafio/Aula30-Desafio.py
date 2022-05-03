""""
Cria um contador que a cada volta do laço implemente um contador progressivo e outro regressivo
0 10
1 9
2 8
3 7
4 6
5 5
6 4
7 3
8 2
9 1
10 0
"""

'''
minha resolução 
p = 0
s = 10
while p<=10:    
    print(p,s)
    p=p+1
    s=s-1 '''
    
    
#resolução

for r in enumerate(range(10,1,-1)):
    print(r)