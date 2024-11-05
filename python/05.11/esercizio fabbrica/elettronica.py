import prodotto 

class Elettronica(prodotto):
    def __init__(self,nome,costo_produzione,prezzo_vendita):
        super().__init__(nome,costo_produzione,prezzo_vendita)
        self.garanzia = "5 anni"

    def get_garanzia(self):
        return self.__garanzia
    
    def set_garanzia(self,garanzia):
        self.__garanzia = garanzia