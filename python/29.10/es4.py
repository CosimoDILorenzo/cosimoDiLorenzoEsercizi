# Esercizio 4
numeri = [];
ripeti = True

while ripeti:
    numero = int(input("Inserisci un numero intero  "))
    if numero.is_integer():
        numeri.append(numero)

    ripeti = input("Vuoi ripetere ? si/no: ").lower();

    if ripeti != "si":
        break;

massimo = numeri[0]

for num in numeri:
    if num > massimo:
        massimo = num;

print(f"Il valore massimo è {massimo}")

contatore = 0

while contatore < len(numeri):
    contatore += 1

print(f"Nella lista sono presenti {contatore} numeri")

if len(numeri) == 0:
    print("La lista è vuota")
else:
    print(f"Il numero massimo della lista è {massimo} e il numero degli elementi è {contatore}") 