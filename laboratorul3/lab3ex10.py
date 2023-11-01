def loop(mapa):
    vizitate = set()
    rezultat = []
    curenta = 'start'
    while curenta in mapa and curenta not in vizitate:
        vizitate.add(curenta)
        rezultat.append(mapa[curenta])
        curenta = mapa[curenta]
    return rezultat

print(loop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))