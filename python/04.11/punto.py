import math

class Piano_cartesiano:
    def __init__(self):
        self.punti = []

    def start(self):
        while True:
            quantita = int(input("Quanti punti vuoi aggiungere? minimo 2: "))

            if quantita < 2:
                print("Devi inserire almeno due punti. Riprova.")
                continue 
            else:
                count = 0 

                while count < quantita:
                    punto_x = int(input("Digita un punto x: "))
                    punto_y = int(input("Digita un punto y: "))

                    punto_nuovo = Punto(punto_x, punto_y)
                    self.punti.append(punto_nuovo)
                    count += 1  
                break

    def stampa_punti(self):
        for punto in self.punti:
            print(punto)


class Punto:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def muovi_punto(self,dx,dy):
        self.x += dx;
        self.y += dy;

    def distanza_da_origine(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)
    
    def __str__(self):
        return f"x: {self.x}, y: {self.y}"
    

punto1 = Punto(3,4);

punto1.muovi_punto(2,-1)

piano_cart = Piano_cartesiano()

piano_cart.start()
piano_cart.stampa_punti()

# print(punto1.x,punto1.y)