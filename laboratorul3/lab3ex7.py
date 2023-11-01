def operatii(*sets):
    rezultate = {}
    pereche = list(sets)
    for i in range(len(pereche)):
        for j in range(i + 1, len(pereche)):
            set_a = pereche[i]
            set_b = pereche[j]
            key = f"{set_a} | {set_b}"
            rezultate[key] = set_a | set_b
            key = f"{set_a} & {set_b}"
            rezultate[key] = set_a & set_b
            key = f"{set_a} - {set_b}"
            rezultate[key] = set_a - set_b
            key = f"{set_b} - {set_a}"
            rezultate[key] = set_b - set_a
    return rezultate

primaLista = set(input("Introdu mai multe variabile: ").split())
aDouaLista = set(input("Introdu mai multe variabile: ").split())
raspuns = operatii(primaLista, aDouaLista)
for key, value in raspuns.items():
    print(f"{key}: {value}")