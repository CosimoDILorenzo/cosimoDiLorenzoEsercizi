from prodotto import Prodotto 

class Elettronica(Prodotto):
    def __init__(self,nome,costo_produzione,prezzo_vendita):
        super().__init__(nome,costo_produzione,prezzo_vendita)
        self.garanzia = "5 anni"

    def get_garanzia(self):
        return self.__garanzia
    
    def set_garanzia(self,garanzia):
        self.__garanzia = garanzia  

    def info_prodotto(self):
        print(f"Il prodotto elettronico chiamato {self.nome}, il costo di produzione è di {self.costo_produzione} e si vende a {self.prezzo_vendita}")