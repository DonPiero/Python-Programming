def is_palindrome(numar):
    return str(numar) == str(numar)[::-1]

numarPrimit = int(input("Introdu un numar: "))
rezultat = is_palindrome(numarPrimit)

print(rezultat)