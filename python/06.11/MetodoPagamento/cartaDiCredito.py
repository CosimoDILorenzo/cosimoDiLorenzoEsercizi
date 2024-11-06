from metodoPagamento import MetodoPagamento

class CartaDiCredito(MetodoPagamento):

    def effettua_pagamento(self, importo):
        print(f"Pagamento {importo} effettuato con carta di credito")



mastercard = CartaDiCredito();

mastercard.effettua_pagamento(122)