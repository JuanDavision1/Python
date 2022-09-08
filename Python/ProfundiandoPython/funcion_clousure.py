#un clousure es una funcion que define a otra y la puede regresar
#la funcion anidada puedad acceder a las var locales definidas
#en la funcion principal o externa
#def operacion(a,b):
    #definimos la funcion interna o anidada
#    def sumar():
#        return a+b

    #retornar la funcion
#    return sumar
def operacion(a,b):
    #funcion lambda
    return lambda :a+b


print(f'Rta de la funcion clousere {operacion(5,4)()}')