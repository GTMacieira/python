"""
1 - Crie uma função que exibe uma saudaçõa com os parametros saudação e nome. 
"""
def saudacao(saud ='Olá', nome ='Usuário'):
    return(f'{saud} {nome}')

var = saudacao('Bem vindo!', 'Guilherme')
print(var)


"""
2 - Crie uma função que recebe 3 números como porâmetros e exibe a soma entre eles
"""
def soma(n1, n2, n3):
    return n1 + n2 + n3

result = soma( 1, 7, 7)
print(result)

"""
3 - Crie uma função que 2 números. O prmeiro é o valor e o segundo um percentual (ex 10%). Retorne (return) o valor
do primeiro número somado ao aumento do percentual do mesmo.
"""

def percent( int , per):
    return int + int * per / 100

result = percent ( 15, 100)
print (result)

"""
4 - Fizz Buzz - Se o parâmetro da função for divisível por 3, retorne fizz, se o parâmetro da função for divisivel 
por 5, retorne buzz. Se p parâmetro da função for divisivel por 5 e por 3, retorne FizzBuzz, caso contrário, retorne
número enviado.
"""""
def FizBuzz (num):
    rest = num % 3
    rest2 = num % 5
    if rest == 0 and rest2 == 0:
        return('FizzBuzz')
    if rest == 0:
        return('fizz')
    if rest2==0:
        return('buzz')
    return('Número enviado')


ret = FizBuzz(2)
print(ret)

    