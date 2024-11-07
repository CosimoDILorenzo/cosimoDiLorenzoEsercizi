class Furgone:
    def __init__(self,colore,capacita_carico):
        self.colore = colore
        self.capacita_carico = capacita_carico

    def carica(self,peso):
        if peso > self.capacita_carico:
            return f"Il peso da lei selezionato è troppo grande"
        else:
            return f"Caricati {peso}kg di merce"
        
    def scarica(self):
        if self.capacita_carico > 0:
            return f"Stai scaricando"
        else:
            return f"Non hai nulla da scaricare"
         
    def metodo_specifico(self):
        return f"Il furgone fa qualcosa"
    
    def info_veicolo(self):
        return f"Il furgone che stai guidando è di colore {self.colore} ed ha una capacità di carico di {self.capacita_carico}kg"


furgone = Furgone("grigio",12)

print(furgone.carica(14))
print()
print(furgone.scarica())
print()
print(furgone.info_veicolo())
