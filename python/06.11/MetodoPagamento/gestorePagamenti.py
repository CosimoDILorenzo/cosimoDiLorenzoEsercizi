from metodoPagamento import MetodoPagamento
from bonificoBancario import BonificoBancario
from payPal import PayPal
from cartaDiCredito import CartaDiCredito

class GestorePagamenti:
    def __init__(self, metodo_di_pagamento = MetodoPagamento):
        self.metodo_di_pagamento = metodo_di_pagamento

    def effettua_pagamento(self,importo):
        self.metodo_di_pagamento.effettua_pagamento(importo)


bb = BonificoBancario()
pay = PayPal()
carta = CartaDiCredito()

gestore = GestorePagamenti(bb)

gestore.effettua_pagamento(200)