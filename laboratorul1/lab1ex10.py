def count_words(mesaj):
    cuvinte = mesaj.split()
    return len(cuvinte)

mesajPrimit = input("Scrie ceva: ")
rezultat = count_words(mesajPrimit)

print(f"Mesajul primit are: {rezultat} cuvinte.")