#extender funcionalidad
#es una funcion que recibe una funcion y regresa otra
#se extiende funcionalidad
#1.Funcion decorador(a)
#2.Funcion a decorar(b)
#3.Funcion decorada(c)
def funciondecorador_a(Funcion_a_decorar_b):
        def funcion_decorada_c():
            Funcion_a_decorar_b()

        return funcion_decorada_c()

@funciondecorador_a
def mostrar_mensaje():
    print('Hola desde Funcion mensaje')

mostrar_mensaje()
