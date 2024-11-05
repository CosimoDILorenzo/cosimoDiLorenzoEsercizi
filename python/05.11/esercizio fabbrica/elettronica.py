import prodotto 

class Elettronica(prodotto):
    def __init__(self,nome,costo_produzione,prezzo_vendita,garanzia):
        super().__init__(nome,costo_produzione,prezzo_vendita)
        self.garanzia = garanzia