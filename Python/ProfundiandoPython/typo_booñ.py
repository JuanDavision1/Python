#bool contiene true y false
#tipo numericos False para 0 y true demas valores
valor = 0
resultado = bool(valor)
print(f'valor {valor}, resultado :{resultado}')
valor = 12
resultado = bool(valor)
print(f'valor {valor}, resultado :{resultado}')
#tipo str, False para '', true demas valores
valor = ''
resultado = bool(valor)
print(f'valor {valor}, resultado :{resultado}')
valor = 'dddd'
resultado = bool(valor)
print(f'valor {valor}, resultado :{resultado}')
#tipo colecciones, False para colecciones vacias y terue para el resto
#lista
valor = []
resultado = bool(valor)
print(f'valor {valor}, resultado :{resultado}')
valor = [1,2,2]
resultado = bool(valor)
print(f'valor {valor}, resultado :{resultado}')

if bool(''):
    print('regreso verdadero')
else:
    print('regreso falso')