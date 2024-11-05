import prodotto 

class Abbigliamento(prodotto):
    def __init__(self,nome,costo_produzione,prezzo_vendita,materiale):
        super().__init__(nome,costo_produzione,prezzo_vendita)
        self.materiale = materiale

    