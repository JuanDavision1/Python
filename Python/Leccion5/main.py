#funciones
"""""
def mi_Funcion(nombre, apellido):
    print(nombre,apellido)

mi_Funcion('juan', 'pereza')
mi_Funcion('karla', 'pfff')

def sumar(a,b) -> int:
    return a+b

print(sumar(4,5))

#pasar argumentos sin saber el numero de elementos a recibir
# se convierte a una tupla
# con el asterisco se indica que es una tupla..
def ListaNombres(*nombres):#es muy usado usar *args cuando se pasan muchos elementos a un parametro
    for nombre in nombres:
        print(nombre, end=' ')

ListaNombres('juan','pedro','kk','lore','espe','dd')
ListaNombres('jjj','dd')

def sumarnros(*args):
    resultado =0
    for i in args:
        resultado += i
    return resultado

print(f'suma:{sumarnros(5,6,7,3,4)}')

def multiplycar(*args):
    resultado = 1
    for valor in args:
        resultado *= valor
    return resultado

print(f'Multiplicacion :{multiplycar(3,5,15)}')

# para indicar que se quiere pasar un diccionario
def listaTerminos(nombre, *nombres, **kwargs):#argumentos fijos, argumentos tipo tupla, argumentos como diccionario 
    for llave,valor in kwargs.items():
         print(f'{llave}:{valor}')

listaTerminos(IDE= 'hola',
              Kk ='jj'
)

#recibir una lista de elementos

def desplegarnombres(nombres):
    for nombress in nombres:
        print(nombress)

nombres =['juan','gg','ff']
desplegarnombres(nombres)
desplegarnombres([10,11,12])
desplegarnombres((0,1))


#Funciones recursivas
#LLAMADA ASI MISMA
def factorial (numero):
    if numero == 1:
        return 1
    else:
       return numero * factorial(numero-1)

print(f'Factorial es : {factorial(2)}')

###ejercicio
def funcionrecursiva(numeroo):
    if numeroo >= 1:
        print(numeroo)
        funcionrecursiva(numeroo-1)
    if numeroo <= 0:
        return 0

funcionrecursiva(5)
"""
def calculadora(sinimpuesto,Conimpuesto):
   return sinimpuesto + sinimpuesto *(Conimpuesto/100)




sinimpuesto=float(input('Proporcione el pago sin impuesto  '))
Conimpuesto=float(input('Proporcione el impuesto  '))

print(f'Pago con Impuesto:{calculadora(sinimpuesto,Conimpuesto)}')

#convertidos de temperatura
def definir(valor):
    if valor== 1:
        CaF(valor)
    elif valor == 0:
        FaC(valor)
def CaF(celsius):

    return celsius * 9/5 +32


def FaC(Faren):
    return (Faren-32) *5 / 9

valor = float(input('Proporcione lo que desea hacer 1. Celsuis a F o 2. Fare a celsius'))
resultado = CaF(valor)
resultado2 = FaC(valor)
print(f'{resultado:.2f}')
print(resultado2)
#SECCION 8 COMPLETADAAA