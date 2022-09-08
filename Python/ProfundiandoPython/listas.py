#listas mutables
nombre = ['Juan' ,'kdkd','dkddokd']
nombre2= 'laura mms jsjsj ooeo '.split()
#suma lista
print(f'sumar listas{nombre +nombre2}')
#extender una lista sobre otra lista
nombre.extend(nombre2)
print(f'extender lista uno con las 2{nombre}')

#indice de listas
numeros1 =[1,9,3,4,5,5,5,5]
print(numeros1.index(3))
#invertir el orden de una lista
numeros1.reverse()
print(f'Lista al reves{numeros1}')
numeros1.sort()
print(f'ordenar los elementos{numeros1}')
numeros1.sort(reverse=True)
print(f'ordenar los elementos al reves{numeros1}')
#ovtener val min y max de una lista
print(f'valor minimo {min(numeros1)}')
print(f'valor maximo{max(numeros1)}')
#copiar elementos de una lista
numeros3= numeros1.copy()
print(numeros3)
#copiar contenido de una lista
numeros2= numeros1[:]
print(numeros2)
#multiplicacion de listas
lista_multi = 5*[[2,5]]
print(lista_multi)
#matrices en python
matriz =[[10,20],[30,40,50],[60,70,80,90]]
print(f'matriz original{matriz}')
print(f'renglon 0 columna 0 {matriz[0][0]}')
print(f'renglon 2 columna 2 {matriz[2][2]}')

#ordenar una lista de listas
lista_listas =[[10,14,33,559],[1,3,2],[2,2,2,2,2,2,2]]
lista_listas.sort(key=len)
print(f'ordenar lista:{lista_listas}')

#build-in sorted
nombre1 = ['juan carlos','ddd','ttt']
nombre1 = sorted(nombre1)
print(nombre1)
# ordenar descendente
nombre1 = sorted(nombre1,reverse = True )
print(nombre1)
#ordenar por la cantidad de caracteres(largo)
nombre1 = sorted(nombre1,key=len)
print(nombre1)
#reversed
nombre1 = reversed(nombre1)
print(list(nombre1))

