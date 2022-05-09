from more_itertools import divide
from sympy import fu


def funcao(var):
    print('se este print etiver abaixo do return ele não sera exibido')
    return var #comentar para none, sempre return é encontrado afunção acaba ali
    
variavel = funcao('ola')

if variavel:
    print(variavel) # se ao chamar uma função, não encontrar return, seu valor é none
else:
    print('nenhum valor')
    
    
def divisao(n1,n2):
    if n2 == 0:
        return
    return n1 / n2

divide= divisao(8,1)

if divide: # realiza verificão se variavel é none(falso) ou há valor (true)
    print(divide)
else:
    print('Conta inválida')

    """
    Funções podem retornar qualquer coisa, inclusive outras funções
    """

