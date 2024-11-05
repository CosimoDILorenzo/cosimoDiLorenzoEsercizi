import prodotto 

class Abbigliamento(prodotto):
    def __init__(self,nome,costo_produzione,prezzo_vendita):
        super().__init__(nome,costo_produzione,prezzo_vendita)
        self.__materiale = "cotone"

    def get_materiale(self):
        return self.__materiale
    
    def set_materiale(self,materiale):
        self.__materiale = materiale

    