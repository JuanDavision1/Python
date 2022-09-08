
# archivos .py == python
# se crea el entorno virtual venv para la version
# mensaje a consola
# mandar info a la consola print
print("hola mundo con pyton")
# enviar un saludo con python
print('Este es mi saludo desde python')
# declaracion y uso de VARIABLES EN PYTHON
# no se indica el tipo de variable
# el programa se ejecuta de arriba hacia abajo
miVariable = 2
print(miVariable)
miVariable = 10
print(miVariable)
x = 20
y = 2
z = x + y
print(x)
print(y)
print(z)
print(x, y, z)
# para saber la direccion de memoria que contain el dato
print(id(x))
nombre = "Juan Mejia"
telefono = 1234454
gmail = 'jdmejia94@'
print(nombre, telefono, gmail)
# tipos de datos
# numericos
# diccionario
# diccionario
# boleano
# set
# tipo secuencia -> strings,list,tuple
x = 10
print(x)
print(type(x))
# se puede poner el tipo, darle una pista, una indicacion
x: str = 'hola mundo'
print(x)
print(type(x))
x = 10.444
print(x)
print(type(x))
x = False
print(x)
print(type(x))
# manejo de cadenas
miGrupoFaborito = "Aerosmith"
comentario = "The best rock band "
# unir cadenas
# print("Mi grupo Favorito es :" + miGrupoFaborito + "" + comentario)
print("Mi grupo favorito :" , miGrupoFaborito, comentario)
# pasar de string a numero
numero1= "1"
numero2= "2"
print("conc" , numero1 + numero2)
print("suma : ", int(numero1) + int(numero2))
# booleano
#decisiones depende de la condicion
mivariablee = True
print(mivariablee)
mivariablee = 1>2
print(mivariablee)
if mivariablee:
    print("resultafo fue verdader")
else:
    print("fue falso ")
# entrada de usuarios
resultado = input("Escribe un mensaje : ")
print(resultado)
# por defecto el input devuelve un str
numero11 = int(input("Escribe un numero : "))
numero12 = int(input("Escribe un numero2 : "))
resultado2 = numero12 + numero11
print("el resultado es :", resultado2)
Mensaje = int(input("Como estuvo tu dia (1-10) : "))
print("Mi dia estuvo : " , Mensaje)
titulo = input("Proporciona el Titulo: ")
Autor = input("Proporciona el Autor: ")
print(titulo, "fue escrito por ", Autor )
#seccion 3 completada
