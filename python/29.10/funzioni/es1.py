import random

def random_num(a = 1, b = 100):
    num_random = random.randint(a,b);
    while True:
        num_utente = int(input("indovina un numero da 1 a 100 "))
        if num_utente != num_random:
            if num_random < num_utente:
                print("Il numero da indovinare è più piccolo")
            else:
                print("il numero da indovinare è più grande")
            print("Numero sbagliato")
            continue
        else:
            print("Numero indovinato, bravo!!")
            break;

random_num()



