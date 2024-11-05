class Libro:
    def __init__(self,titolo,autore,pagine):
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine

    def descrizione(self):
        return f"Il libro {self.titolo} è stato scritto da {self.autore} ed ha {self.pagine} pagine";

    def __str__(self):
        return f"'{self.titolo}' di {self.autore}, ha {self.pagine} pagine";
