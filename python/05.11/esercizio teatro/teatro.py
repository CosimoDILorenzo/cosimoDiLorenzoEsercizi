from posto import Posto
from postoStandard import PostoStandard
from postoVip import PostoVip

class Teatro:
    def __init__(self):
        self.__posti = [];

    def aggiungi_posto(self,posto):
        self.__posti.append(posto)

    def prenota_posto(self,numero,fila):
        for posto in self.__posti:
            if posto.get_numero() == numero and posto.get_fila() == fila:
                posto.prenota()
                print(f"Il posto: {fila} {numero} prenotato")
                break
            else:
                print(f"Il posto: {fila} {numero} è occupato")
                break

    def stampa_posti_occupati(self):
        for posto in self.__posti:
            print(posto)


marco = Posto(5,"A")
cosimo = PostoVip(7,"B","lounge")
simone = PostoStandard(3,"B",5)
teatro1 = Teatro()

print("Aggiungo tre posti")
teatro1.aggiungi_posto(marco)
teatro1.aggiungi_posto(cosimo)
teatro1.aggiungi_posto(simone)

print("prenoto un posto (fila A posto 1)")
teatro1.prenota_posto(5,"C")
print("provo a prenotare un posto occupato")
teatro1.prenota_posto(1,"A")

teatro1.stampa_posti_occupati()


        