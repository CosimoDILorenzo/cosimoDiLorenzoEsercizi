from metodoPagamento import MetodoPagamento

class PayPal(MetodoPagamento):

    def effettua_pagamento(self, importo):
        print(f"Pagamento di {importo} euro effettuato tramite paypal")