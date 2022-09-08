#aqui se imprimer el detalle ya sea del str del gerente o del empleado aqui se aplica polimorfismo
from Empleado import Empleado
from Gerente import Gerente


def Imprimir_detalles(objeto):
    print(objeto)
    print(type(objeto))
 # metodo instance sirve para preguntar si un objeto pertenece a cierta clase
    if isinstance(objeto,Gerente):
        print(objeto._departamento)
Empleado1 = Empleado('Juan',30000000)
Imprimir_detalles(Empleado1)

Gerente1 = Gerente('Karla',34330,'Tecnologia')
Imprimir_detalles(Gerente1)