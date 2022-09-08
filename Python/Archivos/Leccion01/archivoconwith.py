#con with abre y tambien cierra el archivo
from MENEJO_ARCHIVOS import *
with manejoarchivos('prueba.txt') as archivo:
    print(archivo.read())