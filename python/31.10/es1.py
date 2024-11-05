parola_utente = input("scrivi una parola: ").lower();
vocali = "aeiou";

for indice,lettera in enumerate(parola_utente):
    if lettera in vocali:
        print(f"Vocale '{lettera}' trovata all'indice {indice}")

lista = [1,2,2,3,4]
lista_Modificata = {*lista}
print(lista_Modificata)