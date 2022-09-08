#leer contenido libreria
from urllib.request import urlopen
with urlopen('https://www.hostingplus.com.co/blog/archivo-index-html-para-que-sirve-y-como-se-crea/') as mensaje:
# contenido = mensaje.read().decode('UTF-8')
    palabras = []
for liinea in mensaje:
    palabraslinea = liinea.decode('utf-8').split()
    for plabrar in palabraslinea:
        palabras.append(plabrar)
print(palabras)
   # print(contenido)
#with open('Nuevo_archivo.txt','w',encoding='utf-8') as archivo:
    #archivo.write(contenido)
    # centrar un str
titulo =' Sito web de global mentory'
#print(len(titulo))
#print(titulo.center(50,'-'))
#print(len(titulo))
print(titulo.center(len(titulo)+10,'-'))
print(titulo.ljust(50,'*'))
#justificar a la derecha
print(titulo.rjust(50,'*'))
# reemplazar contenido en str
#print(contenido.replace('','-'))
# eliminar caracteres al inicio y final de una cadena
titulo = ' *** Global mentoru ** '
print(titulo,len(titulo))
titulo = titulo.strip()
print(titulo,len(titulo))
titulo = '***Global mentoru ***'.strip('*')
print(titulo)
titulo = '***Global mentoru ***'.lstrip('*')
print(titulo)
titulo = '***Global mentoru ***'.rstrip('*')
print(titulo)