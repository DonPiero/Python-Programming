def ordonareListe(liste):
    def custom_sort_key(criteriu):
        if len(criteriu) > 1 and len(criteriu[1]) >= 3:
            return criteriu[1][2]
        else:
            return ' '

    return sorted(liste, key=custom_sort_key)


liste = [('abc', 'bcd'), ('abc', 'zza')]

rezultat = ordonareListe(liste)
print(f'Listele ordonate arata astfel: {rezultat}.')