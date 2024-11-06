from posto import Posto

class PostoStandard(Posto):
    def __init__(self, numero, fila, costi_aggiuntivi):
        super().__init__(numero, fila)
        self.costi_aggiuntivi =costi_aggiuntivi

    def prenota(self):
        if not self.__occupato:
             print(f"Posto: {self.__fila} {self.__numero} prenotato con successo")
             print(f"Costi aggiuntivi: {self.costi_aggiuntivi}")
        else:
            print(f"Posto: {self.__fila} {self.__numero} già occupato")