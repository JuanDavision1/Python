#Representacion de objetos (str,rep,format)
class persona:
    def __init__(self,nombre,apellido):
        self._nombre = nombre
        self._apellido = apellido

    #repr mas enfocado a programdores
    def __repr__(self):
        return f'{self.__class__.__name__}(Nombre{self._nombre} Apellido : {self._apellido}'
    #str para user final u otros sistemas
    #la implementacion por default llama al metodo repr
    def __str__(self):
        return f'{self.__class__.__name__}: {self._nombre} {self._apellido}'

    def __format__(self, format_spec):
        return f'nombre:{self._nombre}'
persona1 = persona('ddd','ddd')
print(persona1)
print(f'{persona1}')