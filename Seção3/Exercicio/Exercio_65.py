"""
-> É uma lista de listas de números inteiros
-> As listas internas tem i mesmo tamanhp sde 10 elementos
-> As listas inetrnas conteém números entre 1 a 10 e eles podem ser duplicados

Exercício

-> Crie uma função que encontra o primeiro duplicado consideranso o segundo número como a duplicação

        Requisitos:
            A ordem do número dupliucado é considerada a partir da segunda
            ocorência (o número duplicaso em si).
            Exemplo: [1, 2, 3, ->3<-, 2, 1] 3
            Se não encontrar suplicados na lista, retorne -1
"""

lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]

for l1 in lista_de_listas_de_inteiros:
    s = set(l1)
    if len(s) != len(l1):
        repet = len(l1) - len(s)
    else:
        repet = -1
    # for l2 in l1:
    #     i = 0
    #     j = 0
    #     while i < 10:
    #         if j != i:
    #             j = i
    #             if l2 == l1[i]:
    #                 repet += 1
    #         i += 1
    #
    # if repet == 0:
    #     repet = -1

    print(f'{l1} {repet}')
