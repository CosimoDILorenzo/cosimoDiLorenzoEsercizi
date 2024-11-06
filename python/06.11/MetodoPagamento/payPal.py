from metodoPagamento import MetodoPagamento

class PayPal(MetodoPagamento):

    def effettua_pagamento(self, importo):
        print(f"Pagamento {importo} effettuato tramite paypal")