"""
Operadores Lógicos
and, or, not
in e not in
"""

nome = input('Digite um nome: ')
senha = input('Digite a senha: ')

usuario_bd = 'Guilhereme'
senha_bd= '12346'

if nome == usuario_bd and senha_bd == senha:
    print('Você está logado!')
else:
    print('Você não está logado')