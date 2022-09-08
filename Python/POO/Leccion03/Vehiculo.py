class vehiculo :
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return f'Vehiculo: {self.color} {self.ruedas}'

class Coche(vehiculo):
    def __init__(self,color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return f'{super().__str__()} Coche :{str(self.velocidad)}'

class Bicicleta(vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo
    def __str__(self):
        return f' {super().__str__()}  Bicicleta : {self.tipo}'