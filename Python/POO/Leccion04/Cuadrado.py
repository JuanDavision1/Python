from FiguraGeometrica import FiguraGeometrica
from Color import  Color
class Cuadrado(FiguraGeometrica,Color):
    def __init__(self, lado, color):
        # para herencia multiple no se usa el super .init
        # inicializar por clase
        FiguraGeometrica.__init__(self,lado,lado)
        Color.__init__(self, color)

    def area(self):
        return self.alto * self.ancho

    def __str__(self):
        return f'{FiguraGeometrica.__str__(self)} {Color.__str__(self)}'