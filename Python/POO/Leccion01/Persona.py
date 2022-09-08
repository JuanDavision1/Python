#clases
class Persona:
#metodo inicializador es necesario es como un constructor
# args tipo dupla
#kwargs tipo diccoioonario
    def __init__(self,nombre,apellido,edad, *valores, **terminos):
        #self es una referencia al objeto que vamos a crear
        #atributos de instancia
        #el self es atributo de la clase el que esta solo es pasado por parametro
       #el self se puede llamar asi o como this
        self._nombre=nombre
        self.apellido=apellido
        self.edad= edad
        self.valores = valores
        self.terminos = terminos
        # creacion de metodode la clase
    # el self se manda a todos los metodos como instanciaa
    def Mostrar_Detalle(self):
        #como esta dentro de la clase es necesario el self
        print(f'Persona:{self._nombre},{self.apellido},{self.edad},{self.valores},{self.terminos}')


#crear un objeto de la clase no se pasa ningun valor
#esto hace un llamado a la clase persona y de manera indirecta al self por tanto inicializa
# el self no se pasa ya que python lo maneja
persona1= Persona('juan','perex',22,'22332323233',2,2,2,2, m='manzana',p= 'pera')
persona1.Mostrar_Detalle()
#persona1.telefono =2222222
#se crea atributo para el objeto no para la clase
"""""
print(f'Objeto persona 1:{persona1.nombre} {persona1.apellido} {persona1.edad}')
#modificar variables

persona1.nombre='daniel'
persona1.apellido='ggg'
print(f'Objeto persona 1:{persona1.nombre} {persona1.apellido} {persona1.edad}')


persona2 = Persona('Pati','garcia',44)
print(f'Objeto persona 2:{persona2.nombre} {persona2.apellido} {persona2.edad}')
"""