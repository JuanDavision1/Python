class persona:
     def __init__(self, nombre,  edad):
         self.nombre = nombre
         self.edad = edad
         #overside = sobreescribir
            # un metodo en clase padre se vuelve a definir en la clase hjo

     def __str__(self):
            return f'Persona :{self.nombre}  {self.edad}'


#clase hijo entre parentesis la clase de la cual va a heredar
class Empleado(persona):
    def __init__(self,nombre, edad, sueldo):
        # perimite acceder a los metodos de la clase padre
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    def __str__(self):
        #llama el str del padre el super
        return f'{super().__str__()} Sueldo :  {self.sueldo}'

