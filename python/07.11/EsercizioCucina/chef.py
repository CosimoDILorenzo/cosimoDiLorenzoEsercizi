from personaleCucina import PersonaleCucina

class Chef(PersonaleCucina):

    def __init__(self, nome, eta, piatti, specialità):
        super().__init__(nome, eta, piatti)
        self.__specialità = specialità

    def get_specialità(self):
        return self.__specialità
    
    def set_specialità(self,specialità):
        self.__specialità = specialità

    def lavora(self):
        print(f"Lo {Chef.__class__.__name__} {self.get_nome} sta dirigendo la cucina")

    def prepara_menu(self):
        print("Lo Chef sta preparando il menu per la nuova apertura")




