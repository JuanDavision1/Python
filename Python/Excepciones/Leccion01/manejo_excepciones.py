#procesar una excepcion y que el programa no termine abruptamente
#EL bloque try es el bloque con las sentencias que quieres ejecutar. Sin embargo, podrían llegar a haber errores de ejecución y el bloque se dejará de ejecutarse. El bloque except se ejecutará cuando el bloque try falle debido a un error.
from NumeroIdenticosException import NumerosIdenticosException
resutado = None

try:
    a = int(input('Ingrese Dato Uno'))
    b = int(input('Ingrese Dato Dos'))
    #Excepcon personalizada
    if a == b:
        raise NumerosIdenticosException('Numeros Identicoos')
    resutado =  a/b
#despues del except se pone exception
except ZeroDivisionError as zde:
    print(f'Ocurrio un Error{zde}')
except TypeError as e:
    print(f'Ocurrio un Error : {e}')
except Exception as e:
    print(f'Ocurrio un error {e}')
#else se ejecuta en caso de no haber lanzado ninguna excepcion
else:
    print('No se Arrojo Ninguna Excepcion')
    # siempre se ejecute el bloque finally incluso si se lanza un exception
finally:
    print('Ejecucion Finally')
print(f'Resultado {resutado}')
print('continuamos...')

