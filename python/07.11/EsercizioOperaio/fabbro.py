from operaio import Operaio
from abc import ABC, abstractmethod

class Fabbro(Operaio, ABC):

    def __init__(self, nome, eta):
        super().__init__(nome, eta)

    @abstractmethod
    def uso_attrezzo(self):
        pass