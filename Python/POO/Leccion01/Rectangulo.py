class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura


Rectangulo1 =Rectangulo(int(input("Ingresa la Base: ")), int(input("Proporciona la Altura: ")))

print(f'El area es :{Rectangulo1.area()}')