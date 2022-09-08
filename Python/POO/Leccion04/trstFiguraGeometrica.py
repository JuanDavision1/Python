from Cuadrado import Cuadrado
from Rectangulo import Rectangulo
print(f'Creacion Objeto Cuadrado'.center(50,'.'))
cuadrado1 =  Cuadrado(4,'rojo')
cuadrado1.alto = 10
cuadrado1.ancho = 3
print(cuadrado1)
print(f'area cuadrado:{cuadrado1.area()}')
print(f'Creacion Objeto Rectangulo'.center(70,'.'))
rectngulo2 = Rectangulo(3,2 ,'gg')
print(f'calculo del area del rectangulo {rectngulo2.calcular_area()}')
print(rectngulo2)

