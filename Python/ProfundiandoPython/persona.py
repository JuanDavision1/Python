class persona:
    def __init__(self,nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f'Nombre{self.nombre} apellido{self.apellido} , id {hex(id(self)).upper()}'


persona1= persona('juan', 'perez')
print(persona1)