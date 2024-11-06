from metodoPagamento import MetodoPagamento

class CartaDiCredito(MetodoPagamento):

    def effettua_pagamento(self, importo):
        print(f"Pagamento di {importo} euro effettuato con carta di credito")