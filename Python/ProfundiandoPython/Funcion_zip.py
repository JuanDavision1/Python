#funcion zip unir uno o mas iterables
numeros =(1,2,3)
letras = ['a','b','c']
identificadores = 333,222,111,456,666
conjunto = {6,4,3,2,10}
#EL ITERABLE CON MENOS ELEMENTOS SERA EL NRO DE ELEMENTOS QUE TENDRA LA MEZCLA
mezcla = zip(numeros,letras,identificadores,conjunto)
#print(list(mezcla))
#cuando se consumen los elementos del objeto zip se tiene que volver a poner
#print(tuple(zip(numeros,letras)))
#print(type(mezcla))
#iterar en paralelo
for numeros,letra,id,aleatoreo in zip(numeros,letras,identificadores,conjunto):
    print(f'numero{numeros} letra :{letra} identiica :{id} aleatoreo:{aleatoreo}')

nueva_lista = []
#for numero,letra,id,aleatoreo in zip(numeros,letras,identificadores,conjunto):
   # nueva_lista.append(f'{id}-{numero}-{letra}-{aleatoreo}')
#print(nueva_lista)

#unzip
mezcla = [(1,'i'),(1,'o'),(3,'p'),(4,'y')]
numeros,letras = zip(*mezcla)
print(f'Numeros:{numeros} Letras : {letras}')
#ordenamiento usanndo zip
letras =['v','g','r','e','a']
numeros =[1,2,3,55,3]
mezcla = zip(letras,numeros)
print(tuple(mezcla))
#ordenar por letra
print(sorted(zip(letras,numeros)))
#crear un diccionarop con zip a partir de 2 conjuntos
llaves = ['Nombre ' ,'Apellido','Edad']
valores = ['juan','perez',33]
diccionario = dict(zip(llaves,valores))
print(diccionario)

#actualizar un elemento de un diccionario
llave = ['Edad']
nueva_edad = [28]
diccionario.update(zip(llave,nueva_edad))

print(diccionario)

