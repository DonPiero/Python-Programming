def my_function(*argumente, **chei):
    argumenteValori = set(argumente)
    cheiValori = set(chei.values())
    contor = sum(1 for x in argumenteValori if x in cheiValori)
    return contor

print(my_function(1, 2, 3, 4, x=1, y=2, z=3, w=5))