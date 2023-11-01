def liste(a, b):
     intersectie = list(set(a) & set(b))
     reuniune = list(set(a) | set(b))
     diferentaAB = list(set(a) - set(b))
     diferentaBA = list(set(b) - set(a))
     print(intersectie, reuniune, diferentaAB, diferentaBA)


primaLista = list(input("Introdu mai multe variabile: ").split())
aDouaLista = list(input("Introdu mai multe variabile: ").split())

liste(primaLista, aDouaLista)