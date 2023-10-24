def operatiiListe(a, b):
    intersectieListe = list(set(a) & set(b))
    reuniuneListe = list(set(a) | set(b))
    diferentaNormala = list(set(a) - set(b))
    diferentaInversata = list(set(b) - set(a))
    print(intersectieListe, reuniuneListe, diferentaNormala, diferentaInversata)

primaLista = list(input("Introdu mai multe variabile: ").split())
aDouaLista = list(input("Introdu mai multe variabile: ").split())

operatiiListe(primaLista, aDouaLista)