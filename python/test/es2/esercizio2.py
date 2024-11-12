from collections import Counter

class Esercizio2:
    def __init__(self):
        self.__lista = []

    def aggiungi(self,dato):
        self.__lista.append(dato)

    def stampa_unici(self):
        unici = set(self.__lista)
        print(unici)


es2 = Esercizio2()

es2.aggiungi("ciao")
es2.aggiungi("ciao")
es2.aggiungi(2)
es2.aggiungi(5)
es2.aggiungi(2)
es2.aggiungi("saluti")

es2.stampa_unici()
        

