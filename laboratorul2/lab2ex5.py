def matriceModificata(matrice):
    for i in range(0, len(matrice)):
        for j in range(0, len(matrice[0])):
            if i > j:
                matrice[i][j] = 0
    return matrice

matricExemplu = [[1, 2, 3, 4],
                 [5, 6, 7, 8],
                 [9, 10, 11, 12],
                 [13, 14, 15, 16]]

print(matriceModificata(matricExemplu))