def count_set_bits(numar):
    return bin(numar).count('1')

numarPrimit = int(input("Scrie un numar: "))
rezultat = count_set_bits(numarPrimit)

print(f"In formatul binar, bitul 1 apare de: {rezultat} ori.")