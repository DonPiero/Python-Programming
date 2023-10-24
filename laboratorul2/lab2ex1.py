def fibo(n):
     sir = []
     if n <= 0:
         return sir
     elif n == 1:
         sir.append(0)
     else:
         sir.extend([0, 1])
         while len(sir) < n:
            next_number = sir[-1] + sir[-2]
            sir.append(next_number)
     return sir

numar = int(input("Scrie un numar: "))
rezultat = fibo(numar)

print(f"Primele {numar} numere din sirul lui fibonacci sunt: {rezultat}")