perguntas ={
    'pergunta 1':{
        'pergunta':'quanto é 2+2?',
        'respostas':{'a':'1','b':'4','c':'5',},
        'resposta_certa':'b',
    },
    'pergunta 2':{
        'pergunta':'quanto é 3*2?',
        'respostas':{'a':'4','b':'10','c':'6',},
        'resposta_certa':'c',
    },
}
respostas_certas = 0

for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')

    print('Escolha sua resposta:')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')
    resposta_usuario = input('Sua resposta: ')
    print()

    if resposta_usuario == pv['resposta_certa']:
        respostas_certas += 1

quant_perguntas = len(perguntas)
porcent_acertos= respostas_certas / quant_perguntas * 100
print( f'Você acertou {respostas_certas} perguntas, totalizando {porcent_acertos}% das perguntas')
