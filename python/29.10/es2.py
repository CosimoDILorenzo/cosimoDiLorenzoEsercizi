# Esercizio 2
n = int(input("Scrivi un numero: "));
if n > 0:
    while True:
        for i in range(n,-1,-1):
            print(i)
        break
else:
    print("Numero da lei inserito non valido")