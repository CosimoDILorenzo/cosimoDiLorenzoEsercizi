# Create 1 array unidimensionale con 50 valori randomici compresi tra 1 e 1.000 e fate i seguenti calcoli:

# - Calcolo della media;
# - Calcolo della moda;
# - Calcolo della deviazione standard;
# - Trasformatelo in un array 5 X 10


import numpy as np
from scipy import stats

arr_1d = np.random.randint(1,1000,50)

media = np.mean(arr_1d)
moda = stats.mode(arr_1d)
deviazione_standard = np.std(arr_1d)
array_multidimensionale = arr_1d.reshape(5,10)


print(f"La media è {media}")
print(f"La moda è {moda}")
print(f"La deviazione standard è {deviazione_standard}")
print(f"Array trasformato in multidimensionale 5x10:  {array_multidimensionale}")
