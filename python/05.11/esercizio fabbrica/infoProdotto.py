from prodotto import Prodotto
from elettronica import Elettronica
from abbigliamento import Abbigliamento

iPhone = Elettronica("iPhone 13",600,1000)
pantalone = Abbigliamento("Maglia Basic Gucci",50,300)

def info_prodotto(prodotto = Prodotto):
    return prodotto.info_prodotto()

info_prodotto(pantalone)