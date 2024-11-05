class ContoBancario:
    def __init__(self):
        self.__titolare = "Mario"
        self.__saldo = 5000

    def get_titolare(self):
        return self.__titolare
    
    def get_saldo(self):
        return self.__saldo
    
    def set_titolare(self,titolare):
        if titolare.strip():
            self.__titolare = titolare
        else:
            print("Non può essere una stringa vuota")

    def set_saldo(self,saldo):
        self.__saldo = saldo

    def deposita(self,importo):
        if importo > 0:
            self.__saldo += importo
        else:
            print("Importo non valido")    

    def preleva(self,importo):
        if importo < self.get_saldo():
            self.__saldo -= importo
        else:
            print("Fondi insufficienti")

    def visualizza_saldo(self):
        print(self.get_saldo())


conto1 = ContoBancario()

print(conto1.get_titolare())
print("Prendiamo il saldo: ")
print(conto1.get_saldo())
print("Modifichiamo il nome in Carlo")
conto1.set_titolare("Carlo")
print("Controlliamo che il nome sia cambiato")
print(conto1.get_titolare())
print("Modifichiamo il saldo a 2000")
conto1.set_saldo(2000)
print("Controlliamo che il saldo si sia modificato")
print(conto1.get_saldo())
print("Preleviamo 1000")
conto1.preleva(1000)
print("Controlliamo il saldo dopo il prelievo")
conto1.visualizza_saldo()
print("Depositiamo 500")
conto1.deposita(500)
print("Controlliamo il saldo dopo il deposito")
conto1.visualizza_saldo()
print("Mettiamo una stringa vuota al set per controllare che non sia possibile")
conto1.set_titolare("")