class Persona :
    contador_personas =0
    @classmethod
    def generarsiguientevalor(cls):
        cls.contador_personas +=1
        return cls.contador_personas

    def __init__(self ,nombre, edad):
        Persona.contador_personas +=1
        self.id_persona = Persona.contador_personas
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'Persona [{self.id_persona}- {self.edad} ,{self.nombre}]]'

persona1 = Persona('Juan' ,33)
print(persona1)
persona2 = Persona('jj' ,33)
print(persona2)
Persona.generarsiguientevalor()
persona4 = Persona('Maria',44)
print(persona4)
print(f'contador personas: {Persona.contador_personas}')