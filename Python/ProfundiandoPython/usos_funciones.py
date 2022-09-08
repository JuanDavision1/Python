#las funciones son ciudadanas de primera clase
#se definen en donde se quiera


#definir funcion
def sumar(a,v):
    return a +v

#asignar a una funcion a una variable
mi_funcion = sumar
#verificar el tipo
print(type(mi_funcion))
#llamamos la funcion a traves de la variable
resultado = mi_funcion(4,3)
print(resultado)

#funcion como argumento
def operacion(a,b,sumar_arg):
    print(f'resultado sumar:{sumar_arg(a,b)}')
operacion(4,3,sumar)

#retornar una funcion
def retornar_funcion():
    #retomamos una funcion
    return sumar


mi_funcion_retornada = retornar_funcion()
print(mi_funcion_retornada(4,3))