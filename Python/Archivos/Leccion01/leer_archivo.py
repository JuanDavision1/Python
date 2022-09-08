
# r es de solo lectura
#w es de escribir write
# a es de append anexar
try:
    archivo = open('c:\Curso-Python\Python\Archivos\Leccion01\prueba.txt', 'r',encoding='utf8')
    #print(archivo.read())
    #especificar el nro de caaracteres de lectura
    #print(archivo.read(5))
#leer lineas completas
    #print(archivo.readline())
    #iterar el archivo
    #for linea in archivo:
    #  print(linea)
  #  print(archivo.readlines())
    #abrir y clonar info
    archivo2 = open('copia.txt','a',encoding='utf8')
    archivo2.write(archivo.read())
except Exception as e:
    print(e)
finally:
    archivo.close()
    archivo2.close()
    print('fin del archivo')