import re
def convert_to_lowercase_with_underscores(mesaj):
    return re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', mesaj).lower()

propozitie = input("Scrie ceva: ")
rezultat = convert_to_lowercase_with_underscores(propozitie)

print(f"Mesaj modificat: {rezultat}")