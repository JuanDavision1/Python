#funciones anidadas, una dentro de otra
def calculadora(a,b,operacion='sumar'):
    #defini funcion anidadad
    def sumar(a,b):
        return a+b
    def restar(a,b):
        return a-b
    #llamamos a la funcion anidadad
    if operacion =='sumar':
        print(sumar(a,b))
    elif operacion=='restar':
        print(restar(a,b))

calculadora(5,4)