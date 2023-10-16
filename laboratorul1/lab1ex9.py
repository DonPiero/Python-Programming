import re
from collections import Counter
def most_common_letter(mesaj):
    litere = re.findall(r'[a-zA-Z]', mesaj)
    numarLitere = Counter(litere)
    most_common = numarLitere.most_common(1)
    return most_common[0][0] if most_common else None

mesajPrimit = input("Scrie ceva: ")
rezultat = most_common_letter(mesajPrimit)

print(f"Litera: {rezultat} apare cel mai frecvent.")