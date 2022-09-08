#manejo de modulos
#hacer uso de otro modulo/archivo en otro archivo en este caso este
#ponemos en nombre del archivo de donde queremos traerlo que queremos
# import y se importa lo que queramos en este caso una clase
from Encapsulamiento import Persona
print('creacion de objtos'.center(50,'-'))
persona3 = Persona('kak' ,'peresss',33)
persona3.Mostrar_Detalle()
print('Eliminacion de Objetos'.center(30,'-'))
del persona3
    # destructor= liberar recursos de objetos no deseados
