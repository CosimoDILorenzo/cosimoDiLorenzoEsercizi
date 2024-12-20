from personaleCucina import PersonaleCucina

class CuocoLinea(PersonaleCucina):

    def __init__(self, nome, eta, preparazione):
        super().__init__(nome, eta)
        self.__preparazione = preparazione

    def get_preparazione(self):
        self.__preparazione

    def set_preparazione(self,preparazione):
        self.__preparazione = preparazione

    def lavora(self):
        print(f"Il {CuocoLinea.__class__.__name__} {self.get_nome} sta preparando il servizio")

    def cucina_piatto(self):
        print("Sta cucinando")

    def cucina(self,piatto):
        if piatto.lower() == "zuppa":
            self.piatti.append(piatto)
            self.ingredienti.append(["Olio","Pane","Fagioli"])
        else: 
            print("Lo chef cucina solo la zuppa")