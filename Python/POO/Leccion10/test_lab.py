from MundoPc.Computadora import Computadora
from MundoPc.Monitor import Monitor
from MundoPc.Orden import Orden
from MundoPc.Raton import raton
from MundoPc.Teclado import Teclado

teclado1 = Teclado('Hp', 'USB')
Raton2 = raton('Hpdd', 'ddUSB')
Monitor1 = Monitor('qqww', 222)
compu1 = Computadora('hp', Monitor1, teclado1, Raton2)

teclado2 = Teclado('Sss', 'ddd')
Raton3 = raton('dd', 'dsgg')
Monitor4 = Monitor('qdfgfgdqww', 44232343243)
compu2 = Computadora('hpdfgdg', Monitor4, teclado2, Raton3)

teclado44 = Teclado('Sss', 'ddd')
Raton33 = raton('dd', 'dsgg')
Monitor44 = Monitor('qdfgfgdqww', 44232343243)
compu3 = Computadora('hpdfgdg', Monitor44, teclado44 , Raton33)


computadoras1 = [compu1, compu2]
orden1= Orden(computadoras1)

orden1.agregar_compu(compu3)
print(orden1)


computadoras2 = [compu2, compu3]
orden2= Orden(computadoras2)
print(orden2)