from dominio.Pelicula import Pelicula
from Servicio.CatalogoPeliculas import CatalogoPeliculas as cp

opcion = None
while opcion != 4:
    try:
        print('Opciones:')
        print('1.Agregar Peli')
        print('2.Listar peli')
        print('3.Eliminar peli')
        print('salir')
        opcion = int(input('Escribe tu Opcion (1-4)'))
        if opcion == 1:
            nombre_pelicula = input('Ingrese un nombre')
            pelicula = Pelicula(nombre_pelicula)
            cp.agregar_pelicula(pelicula)
        elif opcion ==2:
            cp.listar_peliculas()
        elif opcion ==3:
            cp.eliminaar_peliculas()
    except Exception as e:
        print(f'Ocurrio un error{e}')
        opcion= None
else:
    print('Salimos del Programa')