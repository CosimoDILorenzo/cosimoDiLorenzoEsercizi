# Create 2 array bidimensionali numpy 4x4 con valori interi casuali ed eseguite le seguenti operazioni:

# - Restituite la somma di tutti gli elementi dei singoli array che si trovano nell'ultima riga dalla seconda colonna in poi;
# - Unite i 2 array secondo l'asse 1.

import numpy as np

arr1 = np.random.randint(1,10,(4,4))
arr2 = np.random.randint(1,10,(4,4))


def sum_ultima_riga(arr):
    ultima_riga_seconda_colonna = arr[-1,1:]
    somma = np.sum(ultima_riga_seconda_colonna)
    return somma


array_concatenati = np.concatenate((arr1,arr2), axis = 1)

print(arr2)
print(sum_ultima_riga(arr2))
print()
print(array_concatenati)