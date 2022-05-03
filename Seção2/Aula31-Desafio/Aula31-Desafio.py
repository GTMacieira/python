"""
CPF = 168.995.350-09
__________________________________________________________________________
1 * 10 = 10           #     1 * 11 = 11 <-
6 *  9 = 54           #     6 * 10 = 60
8 *  8 = 64           #     8 *  9 = 72
9 *  7 = 63           #     9 *  8 = 72
9 *  6 = 54           #     9 *  7 = 63
5 *  5 = 25           #     5 *  6 = 30
3 *  4 = 12           #     3 *  5 = 15
5 *  3 = 15           #     5 *  4 = 20
0 *  2 =  0           #     0 *  3 =  0
                        #  -> 0 *  2 =  0
        297           #             343
11 - (297 % 11)=11    #     11 - (343 % 11) = 9
1 > 9 = 0             #
Digito 1 = 0          #     Digito 2 = 9

"""

CPF= input('Informe seu CPF (apenas números): ')


digito1 = 0
digito2 = 0
val1 = 0

for r in range(10,1,-1):
        val = (int(CPF[-r - 1]) * r)
        val1 = val1 + val
        
if (11 - (val1 % 11)) > 9:
        digito1 = 0
else:
        digito1 = (11 - (val1 % 11))

#print(digito1)

CPF2 = CPF[0 : 9] + str(digito1)
#print(CPF)

for r in range(9,1,-1):
        val = (int(CPF2[-r - 1]) * r)
        val1 = val1 + val

CPF2 = CPF2 + str(digito2)

if CPF2 == CPF:
        print(f'O CPF {CPF2} é valido')
else:
        print(f'O CPF {CPF} não é valido')
#print(40 + 18 + 56 + 28 + 54 + 35 + 28 + 6 + 16)
  
