"""
1- Crie uma função 1 que recebe uma função2 como parametro e retorne o valor da funação2 executada.
"""

# def ola_mundo():
#     return 'Olá mundo'
#
# def mestre (funcao):
#     return funcao()
#
# executando = mestre(ola_mundo)
# print (executando)


"""
2- Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor sa função2 executada. Faça a função1 executar duas funções que recebem um número diferente de argumentos
"""

def mestre(funcao, *args, **kwargs):
    return funcao(*args,**kwargs)

def fala_oi(nome):
    return f'Oi {nome}'

def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'

executando = mestre(fala_oi, 'Guilherme')
executando2 = mestre(saudacao, 'Guilherme', saudacao='Bom dia!')

print(executando)
print(executando2)


