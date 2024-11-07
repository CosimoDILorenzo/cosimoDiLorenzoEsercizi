class Auto:
    def __init__(self,colore,numero_porte):
        self.colore = colore;
        self.numero_porte = numero_porte

    def suona_clacson(self):
        return f"Stai suonando il clacson"

    def metodo_specifico(self):
        return f"L'auto fa qualcosa"
    
    def info_veicolo(self):
        return f"L'auto che stai guidando è di colore {self.colore} ed ha {self.numero_porte} porte"

panda = Auto("giallo",4)

print(panda.suona_clacson())
print()
print(panda.metodo_specifico())
print()
print(panda.info_veicolo())