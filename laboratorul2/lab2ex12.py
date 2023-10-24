def cuvinteCareRimeaza(cuvinte):
    rime = {}
    for cuvant in cuvinte:
        rima = cuvant[-2:]
        if rima in rime:
            rime[rima].append(cuvant)
        else:
            rime[rima] = [cuvant]
    print(list(rime.values()))

cuvinte = list(map(str, input("Scrie mai multe cuvinte: ").split()))
cuvinteCareRimeaza(cuvinte)