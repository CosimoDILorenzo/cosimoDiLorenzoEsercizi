import prodotto

class Fabbrica:
    def __init__(self):
        self.inventario = {}

    def aggiungi_prodotto(self,prodotto):
        if prodotto in self.inventario:
            self.inventario[prodotto] += 1
        else:
            self.inventario[prodotto] = 1

    def vendi_prodotto(self,prodotto):
        if prodotto in self.inventario:
            self.inventario[prodotto] -= 1
            print(f"Hai venduto un/una {prodotto.nome}, il profitto ricavato dalla vendita è di: {prodotto.calcola_profitto()}")
        else:
            print("Prodotto non disponibile per la vendita")

    def resi_prodotto(self,prodotto):
        if prodotto in self.inventario:
            self.inventario[prodotto] += 1
            print(f"Il reso del/della {prodotto.nome} è stato effettuato correttamente")
        else:
            self.inventario[prodotto] = 1
            print(f"Il reso del/della {prodotto.nome} è stato effettuato correttamente")

    def mostra_inventario(self):
        for prodotto,quantita in self.inventario.items():
            print(f"{prodotto.nome}: {quantita}")


fabbrica1 = Fabbrica();
prodotto2 = prodotto.Prodotto("maglia",19.90,32.90)
prodotto3 = prodotto.Prodotto("pantalone",24.90,49.90)
prodotto4 = prodotto.Prodotto("cappello",11.90,18.90)
prodotto5 = prodotto.Prodotto("cintura",22.90,34.90)

fabbrica1.aggiungi_prodotto(prodotto2)
fabbrica1.aggiungi_prodotto(prodotto2)
fabbrica1.aggiungi_prodotto(prodotto2)
fabbrica1.aggiungi_prodotto(prodotto3)
fabbrica1.aggiungi_prodotto(prodotto4)

fabbrica1.mostra_inventario()
print()
fabbrica1.vendi_prodotto(prodotto2)
print()
fabbrica1.mostra_inventario()
print()
fabbrica1.resi_prodotto(prodotto4)
print()
fabbrica1.mostra_inventario()
print()
fabbrica1.resi_prodotto(prodotto5)
print()
fabbrica1.mostra_inventario()

