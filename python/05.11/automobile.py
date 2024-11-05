class Veicolo:
    def __init__(self,marca,modello):
        self.marca = marca
        self.modello = modello

    def mostra_informazioni(self):
        print(f"Veicolo marca: {self.marca}, modello: {self.modello}")


class Dotazioni_speciali:
    def __init__(self,dotazioni):
        self.dotazioni = dotazioni

    def mostra_dotazioni(self):
        print(f"Dotazioni speciali: {', '.join(self.dotazioni)}")

# Ereditarietà multipla
class AutomobileSportiva(Veicolo,Dotazioni_speciali):
    def __init__(self, marca, modello, dotazioni, cavalli):
        Veicolo.__init__(self,marca,modello)
        Dotazioni_speciali.__init__(self,dotazioni)
        self.cavalli = cavalli

    def mostra_informazioni(self):
        super().mostra_informazioni()
        # Chiamiamo il metodo della prima superclasse
        print(f"Potenza: {self.cavalli} CV")
        self.mostra_dotazioni()


auto_sportiva1 = AutomobileSportiva("Ferrari","F8",["ABS", "Controllo trazione", "Airbag laterali"],720)

auto_sportiva1.mostra_informazioni()
