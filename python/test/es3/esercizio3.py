class PrimaLista:
    def __init__(self):
        self.lista = []

    def riempi_lista(self):
        count = 0
        while count < 5:
            numero = int(input("Scrivi un numero: "))
            self.lista.append(numero)
            count += 1


class SecondaLista:
    def __init__(self):
        self.lista = []

    def riempi_lista(self):
        count = 0
        while count < 5:
            numero = int(input("Scrivi un numero: "))
            self.lista.append(numero)
            count += 1


class RisultatoListe:
    def __init__(self):
        self.risultati = []

    def calcolo(self):
        for i in range(5):
            self.risultati.append(prima.lista[i] + seconda.lista[i])
    
    def stampa_risultati(self):
        print(self.risultati)

prima = PrimaLista()
seconda = SecondaLista()

prima.riempi_lista()
seconda.riempi_lista()

ris = RisultatoListe()
ris.calcolo()
ris.stampa_risultati()



 


