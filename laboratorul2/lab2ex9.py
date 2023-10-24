def stadion(matrice):
    locuri = []
    randuri = len(matrice)
    coloane = len(matrice[0])
    for i in range(1, randuri):
        for j in range(0, coloane):
            if matrice[i][j] < matrice[i-1][j]:
                locuri.append((i,j))
    return locuri


matrice = [[1, 2, 3, 2, 1, 1],
           [2, 4, 4, 3, 7, 2],
           [5, 5, 2, 5, 6, 4],
           [6, 6, 7, 6, 3, 5]]

rezultat = stadion(matrice)
print(f'Urmatorii spectatori nu pot vedea jocul: {rezultat}.')