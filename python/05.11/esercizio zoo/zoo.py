class Zoo:
    def __init__(self):
        self.animali = []

    def crea_animale(self):
        count = 0
        quantita = int(input("Quanti animali vuoi aggiungere ? "))

        while count < quantita:
            nome = input("Inserire il nome dell'animale: ")
            eta = input("Inserire l'età dell'animale: ")
            tipo = input("Inserire tipo animale tra questi: mucca,leone,gatto: ")

            if tipo.lower() == "leone":
                animale_nuovo = Leone(nome,eta)
                self.animali.append(animale_nuovo)
                count += 1
            elif tipo.lower() == "gatto":
                animale_nuovo = Gatto(nome,eta)
                self.animali.append(animale_nuovo)
                count += 1
            elif tipo.lower() == "mucca":
                animale_nuovo = Mucca(nome,eta)
                self.animali.append(animale_nuovo)
                count += 1
            else:
                print("Animale non presente ripeti")
        
    def mostra_animali(self):
        for animale in self.animali:
            print(animale)

class Animale:
    def __init__(self,nome,eta):
        self.nome = nome
        self.eta = eta

    def suono(self):
        print("L'animale emette un suono")


class Leone(Animale):
    def __init__(self, nome, eta):
        super().__init__(nome, eta)

    def caccia(self):
        print(f"Il {self.nome} sta aspettando dietro il cespuglio la sua preda")

    def suono(self):
        print("Il leone ruggisce")

    def __str__(self):
        return f"Leone: {self.nome}, Età: {self.eta} anni"


class Mucca(Animale):
    def __init__(self, nome, eta):
        super().__init__(nome, eta)

    def latte(self):
        print(f"La mucca {self.nome} sta producendo il latte")

    def suono(self):
        print("La mucca mugisce")

    def __str__(self):
        return f"Mucca: {self.nome}, Età: {self.eta} anni"
    


class Gatto(Animale):
    def __init__(self, nome, eta):
        super().__init__(nome, eta)

    def gioca(self):
        print(f"Il gatto {self.nome} sta giocando con un gomitolo di lana")

    def suono(self):
        print("Il gatto miagola")

    def __str__(self):
        return f"Gatto: {self.nome}, Età: {self.eta} anni"




zooSafari = Zoo();
gatto1 = Gatto("Puffy",4)
gatto2 = Gatto("Micio",6)
leone1 = Leone("alex",20)
mucca1 = Mucca("lola",7)

gatto1.gioca()
print()

leone1.suono()
print()

mucca1.latte()

zooSafari.crea_animale()

zooSafari.mostra_animali()