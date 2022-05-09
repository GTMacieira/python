def saudacao(msg = 'Olá', nome ="Usuário"): #def, define uma função, nas quais podem ser atribuidos parametros, (nome ="Usuário", define como padrão, caso não informado)
    nome = nome.replace('e','3') #replace altera o primeiro caracter pelo segundo
    print(f'{msg} {nome}')
    
saudacao("Olá",'Guilherme')
saudacao(nome="João",msg="Dia!") #é possivel mudar a ordem de entrada ao usar nome_pareametro="..." ao chamar a função