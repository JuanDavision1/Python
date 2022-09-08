#profundizando en tuplas

#daclarar variables
a,b ='holas','adios'
print(a,b)
#swap(intercambio)
a,b = b,a
print(a,b)

#regresar multiples valores en una funcion
def minmax(elementos):
    return min(elementos), max(elementos)


min, max = minmax([1,2,3,4,5])
print(min, max)
#regresar la suma de la tupla
resultado = sum((1,2,3,4,5))
print(f'rrsultado:{resultado}')

def sumar(*args):
    return sum(args)

resultado = sumar()

hola ='oye yo soy una perzona fea'
nuevo = hola.split(' ')
print(hola)
for palabra in hola:
    print(palabra)