from personaleCucina import PersonaleCucina

class Chef(PersonaleCucina):

    def __init__(self, nome, eta, specialità):
        super().__init__(nome, eta)
        self.__specialità = specialità

    def get_specialità(self):
        return self.__specialità
    
    def set_specialità(self,specialità):
        self.__specialità = specialità

    def lavora(self):
        print(f"Lo {Chef.__class__.__name__} {self.get_nome} sta dirigendo la cucina")

    def prepara_menu(self):
        print("Lo Chef sta preparando il menu per la nuova apertura")


    def cucina(self,piatto):
        if piatto.lower() == "carbonara":
            self.piatti.append(piatto)
            self.ingredienti.append(["Uova","Pecorino","Guanciale"])
        else: 
            print("Lo chef cucina solo la carbonara")
        




# chef = Chef("Marco",33,[],"italiana")

# chef.cucina("carbonara")

# for piatto in chef.piatti:
#     print(piatto)
