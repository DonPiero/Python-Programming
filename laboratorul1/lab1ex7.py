import re
def extract_number(mesaj):
    numarGasit = re.search(r'\d+', mesaj)
    if numarGasit:
        return int(numarGasit.group())
    else:
        return None

mesajPrimit = input("Scrie ceva: ")
rezultat = extract_number(mesajPrimit)

print(f"Numar gasit: {rezultat}")