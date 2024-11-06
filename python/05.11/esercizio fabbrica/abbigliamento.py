from prodotto import Prodotto 

class Abbigliamento(Prodotto):
    def __init__(self,nome,costo_produzione,prezzo_vendita):
        super().__init__(nome,costo_produzione,prezzo_vendita)
        self.__materiale = "cotone"

    def get_materiale(self):
        return self.__materiale
    
    def set_materiale(self,materiale):
        self.__materiale = materiale

    def info_prodotto(self):
        print(f"Il prodotto di abbigliamento chiamato {self.nome}, il costo di produzione è di {self.costo_produzione} e si vende a {self.prezzo_vendita}")
    