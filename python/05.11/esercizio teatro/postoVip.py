from posto import Posto

class PostoVip(Posto):
    def __init__(self, numero, fila, servizi_extra):
        super().__init__(numero, fila)
        self.servizi_extra = servizi_extra

    def prenota(self):
        if not self.__occupato:
             print(f"Posto Vip: {self.__fila} {self.__numero} prenotato con successo")
             print(f"Servizi extra inclusi: {self.servizi_extra}")
        else:
            print(f"Posto Vip: {self.__fila} {self.__numero} già occupato")

    

        