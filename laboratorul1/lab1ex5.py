def spiral_matrix_to_string(matrice):
    rezultat = []
    while matrice:
        rezultat += matrice[0]
        matrice = list(zip(*matrice[1:]))[::-1]
    return ''.join(rezultat)

matriceExemplu = [
    ['f', 'i', 'r', 's'],
    ['n', '_', 'l', 't'],
    ['o', 'b', 'a', '_'],
    ['h', 't', 'y', 'p']
]
mesaj = spiral_matrix_to_string(matriceExemplu)

print(mesaj)