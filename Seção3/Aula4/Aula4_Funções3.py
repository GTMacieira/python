# def func(*args):
#     print(args)
#     print(args[0])
#     print(args[-1])
#     print(len(args))
    
# func(1,2,3,4,5)

# def func(*args):
#     args=list(args) #casting, caso contrario manteria-se uma tupla
#     args[0]=20
#     print(args)
    
# func(1,2,3,4,5)

def func(*args, **kwargs): '''kwargs são argumentos com palavras chave argumento = "...",args não exibem kwargs e visse e versa'''                        
    args=list(args) #casting, caso contrario manteria-se uma tupla
    args[0]=20
    print(args)
