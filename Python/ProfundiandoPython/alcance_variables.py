#tiempo de vida de una variable(scope)
var_global = 'variable_global'

def imprimir():
    global var_global
    #acceder a variable global
    print(f'variable globar{var_global}')
    #variable local
    var_local ='variable local'
    print('varialbe local ')
    var_global='dddd'
    def funcion_anidada():
        print(f'variable local dentor de una fncion anidad{var_local}')

    funcion_anidada()
imprimir()
