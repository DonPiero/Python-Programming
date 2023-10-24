def partituraMelodiei(noteMuzicale, miscari, start):
    melodie = []
    pozitieActuala = start
    for miscare in miscari:
        pozitieActuala = (pozitieActuala + miscare) % len(noteMuzicale)
        melodie.append(noteMuzicale[pozitieActuala])
    return melodie

noteMuzicale = ["do", "re", "mi", "fa", "sol"]
miscari = numere = list(map(int, input("Introdu mai multe miscari: ").split()))
start = int(input("Scrie o pozitie de start: "))

rezultat = partituraMelodiei(noteMuzicale, miscari, start)
print(rezultat)