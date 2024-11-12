class Autofficina():

    def __init__(self):
        pass

    def ripara_veicolo(self):
        pass

class Veicolo(Autofficina):

    def __init__(self):
        super().__init__()

    def ripara_veicolo(self):
        pass

class Auto(Veicolo):

    def __init__(self):
        super().__init__()

    def ripara_veicolo(self):
        print(f"Sto riparano un auto")

class Moto(Veicolo):

    def __init__(self):
        super().__init__()

    def ripara_veicolo(self):
        print(f"Sto riparano una moto")


class App_riparazioni():

    def __init__(self):
        pass

    def ripara_veicolo(self,veicolo = Veicolo):
        veicolo.ripara_veicolo()


off = Autofficina()

vei = Veicolo()
auto = Auto()
moto = Moto()

gestore = App_riparazioni()

gestore.ripara_veicolo(auto)
gestore.ripara_veicolo(moto)



    