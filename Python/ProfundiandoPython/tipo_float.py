#profundizando tipo float
a= 3.0

#constructor float puede recibir int y str
a = float('10')
#print(f'a:{a:.2f}')
#notacion exponencial (valores postivos o negativos)
a= 3e5
a= 3e-5
#print(f'a:{a:.5f}')
#cualquier calculo que involucre un floart se promueve a float
a= 4+5.0
print(a)
print(type(a))