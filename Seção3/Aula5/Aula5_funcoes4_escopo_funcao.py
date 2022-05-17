variavel = 'Valor' #variavel global

def func():
    print(variavel)

def func2(): #Para trabalhar a variavel dentro da função utiliza-la como argumento.
    #global variavel #Ao usar o global a variavel passa a ser a global (não recomendado)
    variavel='outro valor' #valor so vale par dentro da função, cria uma variavel apensas para a função
    print(variavel)
#Para utilizar as variaveis de outras funções em uma nova função, utilizar return na primeira e atribuí-la a uma variavel    

func()
func2()

print(variavel)
