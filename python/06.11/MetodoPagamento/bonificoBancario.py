from metodoPagamento import MetodoPagamento

class BonificoBancario(MetodoPagamento):

    def effettua_pagamento(self, importo):
        print(f"Pagamento {importo} effettuato tramite bonifico bancario")