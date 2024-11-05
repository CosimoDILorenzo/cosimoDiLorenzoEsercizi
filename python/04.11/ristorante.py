# Creo la classe ristorante
class Ristorante:
    # Mi creo due attributi uno per l'apertura con un valore booleano ed un altro un dizionario vuoto dove poi inserirò i piatti
    aperto = False
    menu = {}

    # Creo un costruttore dove inserisco due variabili che prenderò in input una volta instanziata la classe
    def __init__(self,nome,tipo_cucina):
        self.nome = nome
        self.tipo_cucina = tipo_cucina

    # Funzione descrizione
    def descrivi_ristorante(self):
       print(f"Il ristorante {self.nome} che fa cucina {self.tipo_cucina} è un ottimo ristorante ed ha delle ottime recensioni") 
    
    # Funzione stato apertura
    def stato_apertura(self):
        print("Il ristorante è aperto") if self.aperto == True else print("Il ristorante è chiuso");

    # Funzione apertura ristorante
    def apri_ristorante(self):
        self.aperto = True;
        print("Il ristorante è ora aperto")

    # Funzione chiusura ristorante
    def chiudi_ristorante(self):
        self.aperto = False;
        print("Il ristorante è ora chiuso")

    # Funzione aggiunta al menu
    def aggiungi_al_menu(self,nome_piatto,prezzo):
        self.menu[nome_piatto] = prezzo

    # Funzione rimuovi piatto dal menu
    def togli_dal_menu(self,nome_piatto):
        del self.menu[nome_piatto]

    # Funzione stampa menu
    def stampa_menu(self):
        for piatto,prezzo in self.menu.items():
            print(f"{piatto}: {prezzo}")


cinese = Ristorante("Kiko","cinese")
giapponese = Ristorante("Mo Sushi","giapponese")
italiano = Ristorante("Mulino","italiana")

italiano.aggiungi_al_menu("carbonara",10)
italiano.aggiungi_al_menu("amatriciana",9)
italiano.aggiungi_al_menu("gricia",11)
italiano.aggiungi_al_menu("soute di cozze e vongole",15)
italiano.aggiungi_al_menu("tagliata",22)


italiano.descrivi_ristorante()
print()
italiano.apri_ristorante()
print()
italiano.stato_apertura()
print()
italiano.stampa_menu()
print()
italiano.togli_dal_menu("gricia")
print()
italiano.stampa_menu()
print()
italiano.chiudi_ristorante()
print()
italiano.stato_apertura()

giapponese1 = Ristorante("Mo Sushi","giapponese")