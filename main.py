matriz = [
    [None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None],
    ["n3", None, None, None, None, None, "n2", "n2", "n2", "n2"],
    [None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None],
    [None, None, "n1", "n1", "n1", None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None],
]

LETRAS = "ABCDEFGH" # indexável

qtde_linhas = len(matriz) # 8
qtde_colunas = len(matriz[0]) # 10

print("\n    1  2  3  4  5  6  7  8  9  10")

for i in range(qtde_linhas):

    print(LETRAS[i], end=" | ")

    for j in range(qtde_colunas):
        elemento = matriz[i][j]
        
        if elemento == None:
            print("🌊", end=" ")
        else:
            print("🚢", end=" ")

        if j == 9:
            print()

print()
###############################################

while True:
    print("Navios a serem inseridos: ")
    print("3 navios tamanho 1")
    print("1 navio tamanho 2")
    print("2 navios tamanho 3")

    navios_inseridos = int(input("\nDigite o tamanho do navio a ser inserido: "))

    if (navios_inseridos == 1):
        ...
    elif (navios_inseridos == 2):
        ...
    elif (navios_inseridos == 3):
        ...
    else:
        print("Invalido!")




