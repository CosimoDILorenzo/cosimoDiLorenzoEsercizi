from ristorante import Ristorante

rist = Ristorante()

class Cliente():

    def mostra_menu(self):
        print("\nMenu del ristorante: ")
        for piatto in rist.menu.keys():
            print(f"{piatto}")

    def prendi_ordinazione(self):
        while True:
            
            self.mostra_menu()
            scelta_cliente = input("Scegli un piatto del menu: ").lower()

            if scelta_cliente in rist.menu:
                rist.ordinazioni.append(scelta_cliente)
                print(f"'{scelta_cliente}' è stato aggiunto all'ordinazione.")
            else:
                print("Piatto non disponibile nel menu, per favore scegli un piatto valido.")

            risposta = input("Desidera ordinare ancora? (si/no): ").lower()
            if risposta == "no":
                break

        print("\nLa tua ordinazione:")
        for piatto in rist.ordinazioni:
            print(piatto)




cliente1 = Cliente()

# cliente1.mostra_menu()

cliente1.prendi_ordinazione()