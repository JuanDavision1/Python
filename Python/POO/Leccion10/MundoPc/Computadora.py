from MundoPc.Monitor import Monitor
from MundoPc.Raton import raton
from MundoPc.Teclado import Teclado


class Computadora:
    contador_compu = 0
    def __init__(self, nombre, monitor,teclado, raton):
        Computadora.contador_compu +=1
        self._idCompu = Computadora.contador_compu
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton
    def __str__(self):
        return f'''
        {self._nombre}: {self._idCompu}
        Monitor:{self._monitor}
        Teclado:{self._teclado}
        Raton:{self._raton}
        '''

if __name__ == '__main__':
    teclado1 = Teclado('Hp','USB')
    Raton2 = raton('Hpdd','ddUSB')
    Monitor1 = Monitor('qqww',222)
    compu1 = Computadora('hp',Monitor1,teclado1,Raton2)
    print(compu1)