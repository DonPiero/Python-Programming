def divizibil(x=1, siruri=None, flag=True):
    liste = []
    for sir in siruri:
        caractere = []
        for char in sir:
            codCaracter = ord(char)
            if flag:
                if codCaracter % x == 0:
                    caractere.append(char)
            else:
                if codCaracter % x != 0:
                    caractere.append(char)
        liste.append(caractere)
    return liste


x = int(input("Scrie un numar: "))
siruri = list(map(str, input("Scrie mai multe cuvinte: ").split()))
flag = bool(input("Seteaza un flag: "))

result = divizibil(x, siruri, flag)
print(result)