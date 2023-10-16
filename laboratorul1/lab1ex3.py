def count_occurrences(text1, text2):
    return text2.count(text1)

primaPropozitie = input("Scrie ceva: ")
aDouaPropozitie = input("Scrie altceva: ")
rezultat = count_occurrences(primaPropozitie, aDouaPropozitie)

print(f"Numar aparitii: {rezultat}")