def palindromi(listaNumere):
    contor = 0
    celMaiMare = 0
    for i in listaNumere:
        x = str(i)
        if x == x[::-1]:
            contor += 1
            if i > celMaiMare:
                celMaiMare = i
    print(contor, celMaiMare)

listaNumere = list(map(int, input("Introdu mai multe numere: ").split()))
palindromi(listaNumere)
