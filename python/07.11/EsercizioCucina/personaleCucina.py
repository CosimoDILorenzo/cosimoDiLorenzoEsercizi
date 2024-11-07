class PersonaleCucina:
    def __init__(self,nome,eta,piatti = []):
        self.__nome = nome
        self.__eta = eta
        self.piatti = piatti

    def get_nome(self):
        return self.__nome
    
    def get_eta(self):
        return self.__eta
    
    def set_nome(self,nome):
        self.__nome = nome

    def set_eta(self,eta):
        self.__eta = eta

    def lavora(self):
        pass