#profundizando en diccionarios
#los dic guardan orden
diccionario ={'Nombre':'JUan','aplledio':'perez'}
print(diccionario)
#los dic son mutables pero las llaves deben ser inmutables
#diccionario ={[1,2]:'valorq'}
#diccionario ={(2,3):'valor'}
#se agregta una llave si no se encuentra en el dic
diccionario['Departamento']='Sistemas'
print(diccionario)

#no hay valores duplicados en las llaves de un diccionaerio si ya existe se e¿reemplaza
diccionario['Nombre'] ='Juan Calso'
print(diccionario)

# recuperar eelemtos de un diccionario
#indicando la llave
print(diccionario['Nombre'])
# sino encuentra la llave llanza una excepcion
#metodo get recuepera una llave, si no existe lanza una excepcion
#ademas se puede regresar un valor en caos de no existir la llave
print(diccionario.get('Nombre','No se encontro la llave'))


#set default si modicia el dic , ademas se agerefa un valor por default
nombre = diccionario.setdefault('Nombres','valor por default')
print(nombre)
print(diccionario)
#imprimir un dic pprint
from pprint import pprint as pp
pp(diccionario,sort_dicts=False)