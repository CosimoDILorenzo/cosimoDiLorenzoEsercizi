from operaio import Operaio
from abc import ABC, abstractmethod

class Elettricista(Operaio, ABC):

    @abstractmethod
    def impianto_elettrico(self):
        pass