import math
def find_gcd(nr):
    return math.gcd(*nr)

numere = list(map(int, input("Introdu mai multe variabile: ").split()))
rezultat = find_gcd(numere)

print(f"Cel mai mare divizor comun: {rezultat}")
