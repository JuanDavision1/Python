class Cubo:
    def __init__(self,ancho, alto, profundidad):
        self.ancho = ancho
        self.alto = alto
        self.profundidad = profundidad

    def Volumen(self):
        return self.ancho * self.alto * self.profundidad


ancho = int(input("Proporciona el ancho : "))
alto = int(input("Proporciona el alto : "))
profundidad = int(input("Proporciona el profundidad : "))
Cubo1 = Cubo(ancho, alto, profundidad)

print(f' El volumen es : {Cubo1.Volumen()}')