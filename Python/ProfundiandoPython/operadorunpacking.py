#desempaquetar el continido de una variabble
numeros = [1,2,3]
print(numeros)
print(*numeros)
print(*numeros , sep= ' - ')
#desempaquetando al moemtno de pasar un parameto a una funcion
def suma(a,b,c):
    print(f'Resultado {a+b+c}')


suma(*numeros)

#extraer algunos elementos de una lista
mi_lista =[1,2,3,4,5,6]
a,*b,c,d  = mi_lista
print(a,b,c,d)
#unir listas
lista1 = [1,2,3]
lista2= [4,5,6]
lista3 = [lista2, lista1]
print(lista3)
lista3= [*lista1, *lista2]
print(f'nir lista{lista3}')
#unir diccionarios
dic={'a':1,'b':2, 'c':3,}
dic2 = {'d':4,'e':5}
dic3 ={**dic,**dic2}
print(dic3)
#construir una lista a partir de un str
lista =[*'Hoalaaa']
print(lista)
print(*lista)
