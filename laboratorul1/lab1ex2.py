def count_vowels(t):
    v = "aeiouAEIOU"
    return sum(1 for char in t if char in v)

mesaj = input("Scrie ceva: ")
rezultat = count_vowels(mesaj)

print(f"Numar vocale in text: {rezultat}")