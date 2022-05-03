"""
Criar variáveis para nome (str), idade(int),
altura(float) e peso (float) de uma pessoa
Criar variável com ano atual (int)
Obter o ano de nascimento da pessoa (baseado nai dade e no ano atual)
Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
Exibir textos fo F-string

Fulano tem X anod, Y altura e peasa PKg.
O IMC de Fulado é IMC
Fulano nasceu em ANO
"""
nome = "Fulano"
idade = 28
altura = 1.70
peso = 83.00
ano_Atual= 2022
ano_Nasc = ano_Atual-28
imc= peso/altura**2

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}Kg')
print(f'O IMC de {nome} é {imc:.2f}')
print(f'{nome} nasceu em {ano_Nasc}')
