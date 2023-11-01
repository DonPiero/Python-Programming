def tupla(lista):
    a = set()
    b = set()
    for element in lista:
        if element in a:
            b.add(element)
        else:
            a.add(element)
    return a, b

listaTastatura = list(input("Introdu mai multe variabile: ").split())
print(tupla(listaTastatura))