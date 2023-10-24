from collections import Counter

def contor(x, *liste):
    listeCombinate = []
    for lista in liste:
        listeCombinate.extend(lista)
    contorVariabile = Counter(listeCombinate)
    sir = [item for item, aparitii in contorVariabile.items() if aparitii == x]
    return sir


primaLista = list(input("Introdu mai multe variabile: ").split())
aDouaLista = list(input("Introdu mai multe variabile: ").split())
aTreiaLista = list(input("Introdu mai multe variabile: ").split())
aPatraLista = list(input("Introdu mai multe variabile: ").split())
x = int(input("Introdu o variabila: "))

rezultat = contor(x, primaLista, aDouaLista, aTreiaLista, aPatraLista)
print(rezultat)