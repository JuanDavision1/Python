#simulacion de sobrecarga de constructores en python
#otras formas de crear objetos
class Persona:
    def __init__(self,nombre, apellido):
        self._nombre= nombre
        self._apellido = apellido

    @classmethod
    #con el cls se llama al metodo init
    def crearpersona_vacia(cls):
        return cls(None,None)

    @classmethod
    def crearpersona_valores(cls,nombre,apellido):
        return cls(nombre,apellido)
    def __str__(self):
        return f'Nombre:{self._nombre} Aplledio{self._apellido}'


persona1 = Persona('ja','s')
print(persona1)
persona_vacia = Persona.crearpersona_vacia()
print(persona_vacia)
persona_valor = Persona.crearpersona_valores('karla','ddd')
print(persona_valor)
