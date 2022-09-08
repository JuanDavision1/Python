#condicion = True

#while condicion:
 #   print('ejecutando ciclo while')

#else:
  #  print('fin del ciclo while')
"""""
contador = 0
maximo = 5
while contador<maximo:
    print(contador)
    contador += 1 # contador = contador +1
else:
    print('fin ciclo while')

minimo = 0
contador= 5
while contador >= minimo:
    print(contador)
    contador -= 1
else:
    print('fin')

cadena= "hola"

for letra in cadena:
    print(letra)
else:
    print('fin')

for letra in 'holanda':
    if letra == 'a':
        print(f'la letra encontrada :{letra}')
        break
else:
        print('fin')
 """

 #range= rango
# imprime los elemetos de 0 a 6 el rango establecido
"""
for i in range(10):
    if(i % 2 == 0):
        print(f'valor:{i}')
 
# palabra continue
for i in range(6):
    if(i % 2 != 0):
        #continue ejecuta la siguiente iteracion y ya no las lineas siguientes , break termina todo esta sigue pero en la otra iteracion
        continue
    print(f'valor:{i}')

 #Listas en python
nombre = ["juan", "karla", "pedro", "maria", 0, True]
#imprimir
print(nombre)
#acceder a cada elemento
print(nombre[0])
print(nombre[1])
#acceder a elementos inverso
print(nombre[-1])
#imprimir un rango
print(nombre[0:2])
#ir de inicio a indice (sin incluirlo)
print(nombre[:3])# ESE ESPACIO SE INIDICA EL INICIO
print(nombre[1:])
# cambiar un valor
nombre[3] ='kk'
print(nombre)
#iterar la lista
for i in nombre:
    print(i)
else:
    print('no existen mas nombres en la lista')
# preguntar la longitud
#length = len
print(len(nombre))
#agregar un elemento
nombre.append('lorenzo perro')
print(nombre)
# insertar un eleemnto en un indice en especifico
nombre.insert(1, 'octavio')
print(nombre)
#REMOVER UN ELEMENTO
nombre.remove('octavio')
print(nombre)
#remover el ultimo elemento
nombre.pop()
print(nombre)
#ELIMINAR EN UN IINDICE INDICADO
del nombre[0]#del = delete
print(nombre)
#limpiar la lista
nombre.clear()
print(nombre)
#borrar la lista por completo}
del nombre
print(nombre)

for hoal in range(11):
    if(hoal % 3 == 0):
        print(hoal)
  
rango = range(2, 7)

for i in rango:
    print(f'= {i}')

# ultimo eleemtno es el incremento de 2 en 2
rangoi = range(3, 11,2)
for i in rangoi:
        print(f': {i}')

# una tupla es como una lista
#sigue c¿guardando los elementos que se van almacenando pero no se pueden modificar
#no agregar ni modificar ni eliminar
frutas = ("naranja" , "platano", "guayaba")
# saber el largo
print(len(frutas))
# aceder a un elemento
print(frutas[0])
#navegacion inversa
print(frutas[-1])
#rango
print(frutas[0:2])#sin incluir el ultimo indice
for i in frutas:
    print(i , end=' ')
    #end para que quede todo en una misma linea

#convertir una tupla a lista
frutalista = list(frutas)
frutalista[0]='pera'
#convertir una  lista a tupla
frutas = tuple(frutalista)
print('\n',frutas)
del frutas
print(frutas)

tupla=(13,1,8,3,2,5,8)
milista = list(tupla)
lista= []
for i in milista:
    if(i<5):
       lista.append(i)

tupla = tuple(lista)
print(tupla)
"""
#set en python = coleccion que no mantiene un orden , no tiene elementos duplicados
# no se pueden modificar pero si agregar y eleminar

#set
planetas ={'marte','jupiter', 'venus'}
print(planetas)
#largo
print(len(planetas))
#revisar si un elemento esta presente
print('marte' in planetas)
# agregar un elemento
planetas.add('tierra')
print(planetas)
#no elementos dplicados
planetas.add('tierra')
print(planetas)
# eliminar elementos posiblemente arrojando error
planetas.remove('tierra')
print(planetas)
# eliminar elementos  sin posible arrojo de error
planetas.discard('jupiter')
print(planetas)
#  limiar el set
planetas.clear()
print(planetas)
#diccionarios en python
# es como una lista con un valor asociado
#dic(key,value)
diccionario = {
    'IDE':'Integrated development Enviroment',
    'OOP':'Object Oriented Programming',
    'DBMS': 'DataBase Management System'
}
print(diccionario)
#largo
print(len(diccionario))
#acceder a un elemento(key)
print(diccionario['IDE'])
#otra forma de recuperar un elemento
print(diccionario.get('OOP'))
#modificar elementos
diccionario['IDE'] ='integrated development enviroment'
print(diccionario)
#recorrer elementos
for termino,valor in diccionario.items():
    print(termino,valor)

for termino in diccionario.keys():
    print(termino)

for valor in diccionario.values():
    print(valor)

#exxistencia de un algun elemento
print('IDE' in diccionario)
print('IdE' in diccionario)
#agregar elemento
diccionario['PK']= 'Primary key'
print(diccionario)
#remoover elemento
diccionario.pop('DBMS')
print(diccionario)
#limpiar
diccionario.clear()
print(diccionario)
#eliminar el diccionario
del diccionario
print(diccionario)