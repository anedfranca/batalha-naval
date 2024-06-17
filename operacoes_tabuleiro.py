
def printa_tabuleiro(matriz):
    LETRAS = "ABCDEFGH" # indexável

    qtde_linhas = len(matriz) # 8
    qtde_colunas = len(matriz[0]) # 10

    print("\n    1  2  3  4  5  6  7  8  9  10")

    for i in range(qtde_linhas): # range(8) | i = 0, i = 7 | 0

        print(LETRAS[i], end=" | ")

        for j in range(qtde_colunas): # range(10) | j = 0, j = 9 | 2
            elemento = matriz[i][j]
            
            if elemento == None:
                print("🌊", end=" ")
            else:
                print("🚢", end=" ") 

            if j == 9:
                print()

    print()

