class persona:
    def __init__(self , nombre,edad):
        self._nombre = nombre
        self._edad= edad
#sobre carga de suma
    def __add__(self, other):
        return self._nombre + other._nombre
#sobrecarga de resta
    def __sub__(self, other):
        return self._edad - other._edad
persona1 = persona('juan  ',30)
persona2 = persona('pedro',90)
print(persona1 + persona2)
print(persona1 - persona2)
# el objeto que esta de izq se toma como principal y llama al del derecho
