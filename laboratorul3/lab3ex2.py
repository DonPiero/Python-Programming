def dictionar(text):
     contor = {}
     for char in text:
         if char in contor:
             contor[char] += 1
         else:
             contor[char] = 1
     return contor


exemplu = "Ana has apples."
rezultat = dictionar(exemplu)
print(rezultat)