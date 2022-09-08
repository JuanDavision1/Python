
operandoA= 3
operandoB = 2
suma = operandoA + operandoB
print('El resultado de la suma es :', suma)
#otra forma de imprimir variables
print(f'Resultado sum: {suma}')
resta = operandoB-operandoA
print(f'resultado de la resta : {resta}')
multiplicacion = operandoA * operandoB
print(f'el reultado de la multi es: {multiplicacion}')
division = operandoB/operandoA
print(f'el resultado de la division : {division}')
division = operandoB//operandoA
print(f'resultado division entera: {division}')
modulo = operandoA % operandoB
print(f'El residuo division (modulo) : {modulo}')
exponente = operandoB ** operandoA
print(f'resultaod del exponente : {exponente}')
#ejercicio rectangulo
"""""
alto =int(input('ingresa el alto:'))
ancho = int(input('ingresa el ancho :'))
Area = alto * ancho
Perimetro = (alto + ancho)*2
print(f'El Perimetro del Rectangulo{Perimetro} y el',f'Area es: {Area}')
"""
#operadores de asignacion
"""""
miVeriable = 10
print(miVeriable)
#reasignacion
miVeriable= miVeriable+1
print(miVeriable)
#forma reducida
miVeriable += 1
print(miVeriable)
miVeriable -=2
print(miVeriable)
miVeriable *= 3
print(miVeriable)
miVeriable /= 2
print(miVeriable)
#operadores de comparacion
a=4
b=2
resultado = (a == b)
print(f'Resultado del == :{resultado}')
resultado = (a != b)
print(f'Resultado del != :{resultado}')
resultado = (a > b)
print(f'Resultado del > :{resultado}')
resultado = (a >= b)
print(f'Resultado del >= :{resultado}')
resultado = (a < b)
print(f'Resultado del < :{resultado}')
resultado = (a <= b)
print(f'Resultado del <= :{resultado}')
#ejercicio
ingreso = int(input('Ingresa un numero perre :'))
if ingreso % 2 == 0 :
    print(f'El valor de {a} es numero par')
else:
    print(f'El valor de {a} es numero impar')
# ejercicio edad
ingreso2 = int(input('Ingresa tu edad : '))
esAdulto = 18
if ingreso2 >= esAdulto:
    print('Es un adulto')
else:
    print('es menor de edad')
    """
#operadores logicos en python

ab = True
bb = True
Resultado = ab and bb
print(Resultado)
Resultado = ab or bb
print(Resultado)
Resultado = not bb
print(Resultado)

#ejercicio
valor = int(input('Ingresa valor  '))
valMax = 5
valMin = 0
Rango = (valor >= valMin) and (valor <= valMax)
if Rango:
    print('El valor esta dentro del rango')
else:
    print('El valor fuera de rango')
    #vacaciones
vacaciones = False
diadescanso = False
if not (vacaciones or diadescanso):
    print('Tiene cosas por hacer')

else:
    print('puede asistir al juego')

#edad
edad =int(input('Ingresa tu edad:'))

#rangos

if (  20 <=  edad  <= 30) or (30 >=  edad < 40):
    print('Dentro del Rango 20´s o 30s')
#    if veintes:
  #          print('dentro de los 20s')
    #elif treintas:
     #   print('Dentro de los treintas')

else:
    print('no esta en el rango')
valor1 = int(input('Ingresa el numero1 '))
valor2 = int(input('Ingresa el numero2  '))

if valor1 > valor2:
    print(f'El valor {valor1} es mayor a valor {valor2}')
else:
    print(f'El valor {valor2} es mayor a valor {valor1}')

nombre =input('Ingrese nombre: ')
ID =int(input('Ingrese ID: '))
Precio =float(input('Ingrese precio: '))
Envio = input('Indica si es gratuito (True/False):')

if Envio == 'True':
    Envio = True

elif Envio == 'False':
    Envio = False
else:
    Envio= 'Valor Incorrecto escrbie true o false'

print(f'''
Nombre : {nombre}
Id = {ID}
Precio = {Precio}
Envio ={Envio}
''')
#SECCION 4 TERMINADA
