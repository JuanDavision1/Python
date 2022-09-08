#generador de nros del 1 al 5
def generador_numeros():
    for numeros in range(1,6):
        yield numeros
        print('Se reanuda la ejecucion')

#utilizamos el generdador
generador = generador_numeros()
print(f'objeto generador{generador}')
print(type(generador))
#consumimos los valores del generador
for valor in generador:
    print(f'Objeto generado : {valor}')

gen = generador_numeros()
print(next(gen))
#otra forma de consumir un generador
generador = generador_numeros()
while True :
    try:
        valor = next(generador)
        print(valor)
    except Exception as e:
        print('Se termino de iterar')
        break