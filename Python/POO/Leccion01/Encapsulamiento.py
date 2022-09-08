#clases
class Persona:
    def __init__(self,nombre,apellido,edad):
# con el guion bajo se indica que no sm puede acceder directamente al atributo de la clase
#esto es encapsulamiento
# solo podran ser accesibles dentro de la misma clase
        self._nombre=nombre
        self._apellido=apellido
        self._edad= edad
#el decorados modifica el comportamiento del metodo
    # en este caso se modifica el get

    # para acceder a los atribujos de la clse es necesario los atributos get y se
    # get atrabajar el dato
    # set modificarlo / colocarlo
    # property indica que el metodo nombre encapsula ese tributo
    # y solo se accede atraves del metodo
    @property
    #metodos GET
    def nombre(self):
        return self._nombre

    @property
    def apellido(self):
        print("llamando al metodo get")
        return self._apellido

    @property
    def edad(self):
        return self._edad
    ##  metodos SET
    # se pone el nombre del atributo de la clase sin el guion bajo y el .setter
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @apellido.setter
    def apellido(self, apellido):
        print("llamando al metodo set")
        self._apellido = apellido

    def Mostrar_Detalle(self):

        print(f'Persona:{self._nombre} {self._apellido} {self._edad}')
   #metodo destructor
    def __del__(self):
        print(f'persona : {self._nombre} {self._apellido}  {self._edad}')


if __name__ == '__main__':
    # para ejecutar solo las cosas de este modulo
    persona1= Persona('juan','perex',22)
    # como se le indico el property ya no es necesario los parentesis
    # en este caso el edad no se puede modificar es decir read-only
    persona1.apellido =' Corozo'
    print(persona1.apellido)
    persona1.nombre =' Rosa'
    print(persona1.nombre)

    persona1.Mostrar_Detalle()
    # hacer que un tributo solo este disponible para leer, entonces no se le agerga el metodo .setter solo el propertys
    # imprimir el nombre del archivo

