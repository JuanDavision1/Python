#open es para abrir un archi existente o se abre y crear si no existe
try:
    archivo =open('prueba.txt','w',encoding='utf8')
    archivo.write('Agrégamos Info al Archivo \n')
    archivo.write('adios')

except Exception as e:
    print(e)
finally:
    archivo.close()
    print('fin del archivo')
    #archivo.write('nueva info')
