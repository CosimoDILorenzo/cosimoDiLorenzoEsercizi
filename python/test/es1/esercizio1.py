class Esercizio1():

    def __init__(self):
        self.numeri = []
        self.stringhe = []
        self.booleani = []

    

    def aggiungi(self,dato):
        if isinstance(dato, (int,float)):
            self.numeri.append(dato)
        elif isinstance(dato, str):
            self.stringhe.append(dato)
        elif isinstance(dato, bool):
            print("ci sono")
            self.booleani.append(dato)
        else:
            print("Il dato da lei inserito non è basilare")

    def stampa(self):
        scelta_lista = input("Scegli il tipo di lista che vuoi stampare tra: (numeri,stringhe,booleani,tutte) :")
        if scelta_lista == "numeri":
            print(self.numeri)
        elif scelta_lista == "stringhe":
            print(self.stringhe)
        elif scelta_lista == "booleani":
            print(self.booleani)
        elif scelta_lista == "tutte":
            print(f"Lista numeri: {self.numeri}")
            print(f"Lista stringhe: {self.stringhe}")
            print(f"Lista booleani: {self.booleani}")
        else:
            print("Il dato da lei inserito non esiste")


es = Esercizio1()

es.aggiungi(True)
es.aggiungi(False)
es.aggiungi("stringa1")
es.aggiungi("stringa2")
es.aggiungi(1)
es.aggiungi(2)
es.aggiungi(3)


es.stampa()
