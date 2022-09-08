#funcion especial de secuencia de valores
#yeild = producir se manda los valores poco a poco
#suspende la ejecucion de la funcion yeild (producir)
def generador():
    yield 1
    print('se Reanuda la ejecucion')
    yield 2
    print('se Reanuda la ejecucion')
    yield 3

#consumir el generador a demanda
gen = generador()
# con cada llamada consumimos un valor
print(next(gen))
print(next(gen))
print(next(gen))
# si se trata de consumir valores de los que produce el generador
#lanza un error de stopIteration

#consumiendo  valores con ciclo for
gen = generador()
for valor in gen:
    print(f'Numero generado :{valor}')