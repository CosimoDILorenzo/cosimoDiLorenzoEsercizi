from metodoPagamento import MetodoPagamento

class BonificoBancario(MetodoPagamento):

    def effettua_pagamento(self, importo):
        print(f"Pagamento di {importo} euro effettuato tramite bonifico bancario")