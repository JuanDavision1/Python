# Expresion generadora (es uu generador anonimo)
multiplicarcion = (valor*valor for valor in range(4) )
print(multiplicarcion)
print(next(multiplicarcion))
print(next(multiplicarcion))
print(next(multiplicarcion))
print(next(multiplicarcion))

#tambien se puede pasar una expresion generadora a una funcion (sin parentesis)
import math
suma = sum(valor+valor for valor in range(4))
print(f'resultador de suma{suma}')
#tambien se puede usar una lista o cualquier otro iterador
lista = ['juan','parez']
generador = (valor for valor in lista)
print(next(generador))
print(next(generador))
#crear un string a partir de un generador creado a partir de una lista
lista =['jdd','lll']
contador = 0
def incrementar():
    global contador
    contador+=1
    return contador

# la primera parte es el yield y la segunda es el for entre parentesis
generador =(f'{incrementar()}.{nombre}' for nombre in lista)
list = list(generador)
print(lista)
cadena = ','.join(lista)
print(f'cadena generada{cadena}')