class Monitor:
    contador_monitores = 0

    def __init__(self,  marca,tamaño):
        Monitor.contador_monitores +=1
        self._idMonitor = Monitor.contador_monitores
        self._marca = marca
        self._tamaño = tamaño

    def __str__(self):
        return f'Monitor : Id:{self._idMonitor}, Marca = {self._marca}, Tamaño:{self._tamaño}'

if __name__ == '__main__':
    Monitor1= Monitor('44rr','Hhh')
    print(Monitor1)
    Monitor2 = Monitor('ddd', 'Hhh')
    print(Monitor2)
    print(Monitor.contador_monitores)