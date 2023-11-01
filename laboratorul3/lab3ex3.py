def comparaDictionare(d1, d2):
     if set(d1.keys()) != set(d2.keys()):
         return False
     for key in d1.keys():
         valoare1, valoare2 = d1[key], d2[key]
         if isinstance(valoare1, dict) and isinstance(valoare2, dict):
             if not comparaDictionare(valoare1, valoare2):
                 return False
         elif isinstance(valoare1, (list, set)) and isinstance(valoare2, (list, set)):
             if len(valoare1) != len(valoare2):
                 return False
             for obiect1, obiect2 in zip(valoare1, valoare2):
                 if isinstance(obiect1, (dict, list, set)) and isinstance(obiect2, (dict, list, set)):
                     if not comparaDictionare(obiect1, obiect2):
                         return False
                 elif obiect1 != obiect2:
                     return False
         elif valoare1 != valoare2:
             return False
     return True


dictionar1 = {'a': 1, 'b': [1, 2, {'c': 3}], 'd': {'e': 4}}
dictionar2 = {'a': 1, 'b': [1, 2, {'c': 3}], 'd': {'e': 4}}

rezultat = comparaDictionare(dictionar1, dictionar2)
print(rezultat)