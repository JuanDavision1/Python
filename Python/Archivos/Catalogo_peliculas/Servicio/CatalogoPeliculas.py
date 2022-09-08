import os

class CatalogoPeliculas:
    ruta_archivo = 'peliculas.txt'
#classmethod accede a los atributos de clase como ruta_archivo el static no
    @classmethod
    def agregar_pelicula(cls,pelicula):
        with open(cls.ruta_archivo,'a', encoding='utf8') as archivo:
            archivo.write(f'{pelicula.nombre}\n')

    @classmethod
    def listar_peliculas(cls):
        with open(cls.ruta_archivo,'r',encoding='utf8') as archivo:
            print('Catalogo de peliculas'.center(50,'-'))
            print(archivo.read())

    @classmethod
    def eliminaar_peliculas(cls):
        os.remove(cls.ruta_archivo)
        print(f'Archivo eliminado :{cls.ruta_archivo}')

    # a es agregar informacion
# as es para renombrar la variale que nos regresa en este caso archivo se llamara
