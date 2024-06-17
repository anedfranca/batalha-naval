from operacoes_tabuleiro import * 
from constantes import *

tabuleiro = [
    [None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None],
    ["n3", None, None, None, None, None, "n2", "n2", "n2", "n2"],
    [None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None],
    [None, None, "n1", "n1", "n1", None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None],
]

printa_tabuleiro(tabuleiro)

###############################################

tamanhos_restantes = [3, 1, 5, 2, 2]

while True:
    if (sum(tamanhos_restantes) == 0):
        break

    print("Navios a serem inseridos: ")
    for i in range(len(tamanhos_restantes)):
        if (tamanhos_restantes[i] > 0):
            print(tamanhos_restantes[i], f"navios tamanho {i+1}")

    tam_navio = int(input("\nDigite o tamanho do navio a ser inserido: "))
    coordenada = input("Em qual coordenada será inserido seu barquinho?  Ex: A1\n").upper() # A10

    i = DICT_RELACOES[coordenada[0]] # 0
    j = int(coordenada[1]) - 1

    tabuleiro[i][j] = 'n'

    printa_tabuleiro(tabuleiro)

    if (tam_navio < 1 or tam_navio > 5):
        print("tamanho inválido!!!")
    else:
        baixo = tamanhos_restantes[tam_navio-1] - 1
        if (baixo >= 0):
            tamanhos_restantes[tam_navio-1] -= 1
        else:
            print("tamanho inválido!!!") 




