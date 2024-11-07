# Crea una classe ristorante con una lista di liste chiamata menu e una lista chiamata ordinazione, 
# Nel menu ci devono essere X piatti composti ogniuno da una lista propria di ingredienti, 
# e la lista ordinazione invece e composta dalle singole ordinazioni del cleinte, 
# Servirrà quindi una classe cliente e ogni membro della cucina potrà servire solo X piatti

import itertools

from chef import Chef
from sousChef import SousChef
from cuocoLinea import CuocoLinea
from personaleCucina import PersonaleCucina

class Ristorante():

    def __init__(self):
        self.menu = {}
        self.ordinazioni = []

    def crea_menu(self,personale):
        for piatto in personale.piatti:
            self.menu[piatto] = personale.ingredienti

    def stampa_menu(self):
        for m in self.menu.items():
            print(f"Piatto: {m[0]} - ingredienti: {", ".join(list(itertools.chain(*m[1])))}")


personal = PersonaleCucina("Paolo",33)
chef = Chef("Luca",25,"italiana")
sou = SousChef("Marco",27,"secondi")
cuoco = CuocoLinea("Giacomo",31,"zuppe")

rist = Ristorante()

chef.cucina("carbonara")
sou.cucina("tagliata")
cuoco.cucina("zuppa")

rist.crea_menu(chef)
rist.crea_menu(sou)
rist.crea_menu(cuoco)
rist.stampa_menu()    
