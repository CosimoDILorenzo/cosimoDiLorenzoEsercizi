import libro;

class Biblioteca:
    def __init__(self):
        self.libri = []
    
    def crea_libro(self):
        count = 0;
        quantita = int(input("Quanti libri vuoi aggiungere ? "))

        while count < quantita:
            titolo = input("Inserire il titolo del libro: ")
            autore = input("Inserire l' autore del libro: ")
            pagine = input("Inserire quante pagine ha il libro: ")
            nuovo_libro = libro.Libro(titolo,autore,pagine)
            self.libri.append(nuovo_libro)
            count += 1;
            if count == quantita:
                self.stampa_libri()
    
    def stampa_libri(self):
        for libro in self.libri:
            print(libro)

biblioteca1 = Biblioteca()
biblioteca1.crea_libro()

