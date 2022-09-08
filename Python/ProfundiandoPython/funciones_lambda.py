#funciones lambda
#funcones pequeñas
#funciones anonimas y son pequeñas  una linea de cod
# no es posible asignar una funcion a una variable mi_funcion =def sumar(a,b):return a+b
#con lambda(anonima y una sola linea de cod)
#no es necesario parantecis para parametros
#no se necesita usar la palabra return, debe regresar una experesio
mi_funcion_lambda = lambda a, b: a + b
resultado = mi_funcion_lambda(4,3)
print(resultado)
#funcion lambda que no recibe argumentos (debemos regresar una expresion valida)
mi_funcion_lambda = lambda :'Funcion sin arg'
print(f'llamar funcion lambda sin argumentos{mi_funcion_lambda()}')

#funcion lambda con parametros por default
mi_funcion_lambda = lambda a=2, b=3:a+b
print(mi_funcion_lambda())

#funcion lambda con argumentos variables *args y *kwargs
mi_funcion_lambda = lambda *args,**kwargs: len(args) +len(kwargs)
print(f'Resuktado arg variables :{mi_funcion_lambda(1,2,3,a=3, b=4,c=6)}')

