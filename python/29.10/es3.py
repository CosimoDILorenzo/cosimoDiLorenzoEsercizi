# Esercizio 3

numeri = [];
iterazione = 0;

while iterazione < 5:
    numero = int(input("Inserisci un numero: "))
    numeri.append(numero)
    iterazione += 1;

for num in numeri:
    print(f"La radice quadrata di {num} è {num ** 2}")


