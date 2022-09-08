import mi_clase
from mi_clase import *
#profundiando str

#concatenar en pytonh
#sin la sumatoria en caso de str
#mensaje = 'hpa' 'mundo'
#mensaje += 'iunn' '´pthon'
#print(mensaje)
#sin parentecis porque cuando uno pone parentecis hace llamado a la misma
#help(str.capitalize)
#help(miclas)

#mensaje1= 'hola mundo'
#mensaje2 = mensaje1.capitalize()
#print(f'mensaje 1 {mensaje1}, id : {id(mensaje1)}')
#print(f'mensaje 2{mensaje2},id : {id(mensaje2)}')

tupla = ('hla','gg','ddd','www')
mens =' '.join(tupla)
print(mens)
cadena = ('hla')
cadena1 =' '.join(cadena)
print(cadena1)

cursos =' jav ff eee ee ggtgg '
lista = cursos.split()
print(lista)
cursos =' jav,ff,eee,ee,ggtgg '
lista = cursos.split(',')
print(lista)
#dar formato a un str
#nombre = 'Juan'
#edad = 28
#mensaje_formato = 'Mi nombre es %s y tengo %d años' %(nombre,edad)
#print(mensaje_formato)

#persona = ('karla','gomez',22222)
#mensaje_formato = 'Hola %s %s. Tu sueldo es %.2f'%(persona)
#print(mensaje_formato)
#metodo format
#nombre = 'Juan'
#edad = 28
#sueldo =300000
#mensaje = 'Mi nombre {} edad {} sueldo {:.2f} '.format(nombre,edad,sueldo)

#print(mensaje)

#mensaje ='Nombre {0} Edad {1} Sueldo {2:.2f}'.format(nombre,edad,sueldo)

#mensaje = 'Nombre {n} edad {e} sueldo {s:.2f}'.format(n=nombre, s=sueldo,e = edad)
#print(mensaje)

diccionario ={'nombre':'ivan', 'edad ':33, 'sueldo ':22222 }

mensaje ='Nombre {dic[nombre]}'.format(dic = diccionario)
print(mensaje)

#mutiplicacion de str
resultado= 5*'hola'
print(f'resultado:{resultado}')
#multi de tuplas
resultado = 5*('ff','ggg')
print(f'resultado{resultado}')
#multi listas
resultado = 10*[0]
print(f'resultado:{resultado} , len {len(resultado)}')

#caracteres de escape
resultado = ' Hola \'mundo'
print(f'resultado :{resultado}')

resultado ='se va a eliminar el punto.\b\b\b'
print(f'resultado :{resultado}')

# caracter
reultado ='c:\directorio\\juan'
print(reultado)
#row string
resultado =r'Cadena con \n salto de linea'
print(f'Resultadoo :{resultado}')

#caracteres unicode#unicode table
print('Hola\u0020Mundo')
print('Hola Mundo','\u0041')
corazon = '\u2665'
print(f'Corazon:{corazon}','\u2665')

#caracteres ascii
caracter = chr(65)
print('a mayuscula',caracter)
#literalestipo byte
caracterenbyte = b'hola mundo'
print(caracterenbyte)
mensaje = b'universidad pythoon'
print(mensaje[9])
#DE STRINGS A BYTES Y VICEVERSA
string = 'FFFF programacion'
print(f'String original {string}')

bytes = string.encode('UTF-8')
print(f'bytes codificádás',bytes)
#bytes a string

string2 = bytes.decode('UTF-8')
print(string2)