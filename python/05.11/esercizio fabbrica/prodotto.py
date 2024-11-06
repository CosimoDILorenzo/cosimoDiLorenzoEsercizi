class Prodotto:

    def __init__(self,nome,costo_produzione,prezzo_vendita):
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita

    def calcola_profitto(self):
        return self.prezzo_vendita - self.costo_produzione
    
    def info_prodotto(self):
        print(f"Il prodotto chiamato {self.nome}, il costo di produzione è di {self.costo_produzione} e si vende a {self.prezzo_vendita}")
    

prodotto1 = Prodotto("maglia",19.90,32.90);

print(prodotto1.calcola_profitto())