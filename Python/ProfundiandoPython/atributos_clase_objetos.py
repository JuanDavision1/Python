class persona:
    contador_personas=0
    def __init__(self,nombre,apellido ):
        self._nombre = nombre
        self._apellido = apellido

#Mostrar atributos de un objeto
persona1= persona('Juan','Perez')
#despliega atributos asociados a el objeto
print(persona1.__dict__)

#crear atributos al vuelo es decir en este momento
print(persona1.contador_personas)#atributo de clase
#pero no es posible modificarlo con el objeto,sino con la clase
#este solo se asocia al objeto creado a los demas no se asignara
persona1.contador_personas =10
print(persona1.__dict__)
#ACCEDER A LA VARIABLE DE CLASE
#el atributo anterior ooculta al atributo de clade
print(persona.contador_personas)#atributo de clase
print(persona1.contador_personas)#atributo del objeto 1
#un segundo objeto
persona2= persona('jar','lll')
print(persona2.__dict__)
print(persona2.contador_personas)
#asociar un atributo de clase al vuelo
persona.contador2 =20
print(persona.contador2)