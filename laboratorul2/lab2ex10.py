def ordonareListe(*liste):
    maxim = max(len(lista) for lista in liste)
    listaDePrintat = []

    for i in range(maxim):
        listaDePrintat.append(tuple(lista[i] if i < len(lista) else None for lista in liste))
    print(listaDePrintat)


primaLista = list(input("Introdu mai multe variabile: ").split())
aDouaLista = list(input("Introdu mai multe variabile: ").split())
aTreiaLista = list(input("Introdu mai multe variabile: ").split())
aPatraLista = list(input("Introdu mai multe variabile: ").split())
ordonareListe(primaLista, aDouaLista, aTreiaLista, aPatraLista)