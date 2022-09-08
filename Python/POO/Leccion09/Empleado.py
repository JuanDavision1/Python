#polimorfismo es :  multiples formas en tiempo de ejecucion
class Empleado:
    def __init__(self , nombre, sueldo):
        self._nombre = nombre
        self._sueldo = sueldo

    def __str__(self):
        return f'Empleado : Nombre : {self._nombre} , Sueldo: {self._sueldo}'