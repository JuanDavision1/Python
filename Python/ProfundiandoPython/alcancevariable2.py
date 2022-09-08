#MAS DE FUNCIONES ANIDADAS Y ALCANCE DE VARIABLES

def funcion_externa():
    variablelocal_externa ='variable local externa'

    def funcion_anidadada():
        variable_local_anidad = 'variable local anidada'

        nonlocal variablelocal_externa
        variablelocal_externa ='Noevo valor variable local externa'

    funcion_anidadada()
    print(f'Valor variable local externa{variablelocal_externa}')

funcion_externa()