class Posto:
    def __init__(self,numero,fila):
        self.__numero = numero
        self.__fila = fila
        self.__occupato = True

    def get_numero(self):
        return self.__numero
    
    def get_fila(self):
        return self.__fila

    def prenota(self):
        if not self.__occupato:
            self.__occupato = True
            print(f"Posto {self.__fila} {self.__numero} prenotato con successo")
        else:
            print(f"Posto {self.__fila} {self.__numero} é già occupato")
    
    def libera(self):
        if self.__occupato:
            self.__occupato = False
            print(f"Posto: {self.__fila} {self.__numero} è stato liberato")
        else:
            print(f"Il Posto: {self.__fila} {self.__numero} è già libero")

    def stato_posto(self):
        print(f"Il posto è occupato") if self.__occupato else print(f"Il posto non è occupato") 



    
    