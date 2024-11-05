parola_utente = input("Scrivere una parola: ")
dizionario = {};

for l in parola_utente:
    dizionario[l] = parola_utente.count(l)

print(dizionario)