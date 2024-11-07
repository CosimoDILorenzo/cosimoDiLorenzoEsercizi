from personaleCucina import PersonaleCucina

class SousChef(PersonaleCucina):
    def __init__(self,nome,eta,piatti,preparazione):
        super().__init__(nome, eta, piatti)
        self.__preparazione = preparazione

    def get_preparazione(self):
        self.__preparazione

    def set_preparazione(self,preparazione):
        self.__preparazione = preparazione

    def lavora(self):
        print(f"Il {SousChef.__class__.__name__} {self.get_nome} sta gestendo la brigata")

    def gestisci_inventario(self):
        print(f"Il {SousChef.__class__.__name__} sta gestendo l'inventario")