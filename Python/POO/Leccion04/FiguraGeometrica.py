#ABC= Abstract base class
from abc import ABC, abstractmethod
class FiguraGeometrica(ABC):
    def __init__(self, ancho , alto):
        if self._validar_valor(ancho):
            self._ancho = ancho
        else:
            self._ancho = 0
            print(f'Valor erroneo')
        if self._validar_valor(alto):
            self._alto = alto
        else:
             self._alto = 0
             print(f'Valor erroneo')
    @property
    def ancho(self):
        return self._ancho
    @ancho.setter
    def ancho(self,ancho):
        if self._validar_valor(ancho):
            self._ancho = ancho

    @property
    def alto(self):
        return  self._alto
    @alto.setter
    def alto(self,alto):
        if self._validar_valor(alto):
            self._alto = alto
    @abstractmethod
    def calcular_area(self):
        pass
    def __str__(self):
        return f'Figura Geometrica: {self._ancho}, {self._alto}'
#un guion es quq solo se usa dentro de la clase no fuera
    def _validar_valor(self,valor):
        return True if 0 < valor <10 else False