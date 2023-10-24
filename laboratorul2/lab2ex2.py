
def estePrim(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def numerePrime(numere):
   numere_prime = [n for n in numere if estePrim(n)]
   return numere_prime


numere = list(map(int, input("Introdu mai multe numere: ").split()))
rezultat = numerePrime(numere)

print(f"Numerele prime gasite sunt: {rezultat}")