"""condicion = False


if condicion == True :
    print('condicion verdadera')
elif condicion == False:
    print('Condicoon Falsa')
else:
    print('Condicion No reconocida')"""
"""numero = int(input('Proporciona un valor entre 1 y 3: '))
numeroTexto =''
if numero == 1:
    numeroTexto="Numero Uno"
elif numero == 2:
    numeroTexto = 'Numero dos'
elif numero == 3:
    numeroTexto = 'Numero tres'
else:
    numeroTexto = 'Valor fuera de rango'

print(f'Numero Proporcionado {numero}: {numeroTexto}')"""


#condicion = True

#if condicion:
 #   print('condicion verdadera')
#else
 #   print('condicion falsa')
#Operador ternario
#condicion = False
#print('COndicion verdadera') if condicion else print('condicion falsa')}

mes = int(input('Proporciona mes del año:(1-12):'))
estacion = None
if mes == 1 or mes == 2 or mes == 12:
    estacion ='Invierno'
elif mes == 3 or mes == 4 or mes ==5:
    estacion = 'primavera'
elif mes== 6 or mes==7 or mes== 8:
    estacion ='verano'
elif mes == 9 or mes==10 or mes ==11:
    estacion ='otoño'
else:
    estacion = 'mes incorrecto'

print(f'Para el mes {mes} la estacion es {estacion}')

edad =int(input('Ingresa tu infancia: '))

if  0 <= edad <10:
    print(f'la infancia {edad} es increible...')
elif 10 <= edad <20:
    print(f'Muchos cambios {edad} y mucho estudio ...')
elif 20 <= edad <30:
    print(f'Amor en los {edad}y trabajo ...')

else:
    print('Etapa de vida no reconocida ')

