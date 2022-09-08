#ejemplo atributos publicos , protegidos , privados
class Micalse:
    def __init__(self,publico,protegido,privado):
        self.publico = publico
        self._protegido= protegido
        self.__privado = privado
objeto = Micalse('valor publico','valor protegido','valor privado')
print(objeto.publico)
#modificar el valor publico
objeto.publico='2222'
print(objeto.publico)
#acceso al valor protegido
#solo dentro de la clase o clases hijas
#acceder al valor privado
print(objeto._Micalse__privado)