class DispositivoEntrada:

    def __init__(self, tipoEntrada, marca):
        self._tipoEntrada = tipoEntrada
        self._marca = marca
    @property
    def tipoEntrada(self):
         return self._tipoEntrada

    @tipoEntrada.setter
    def tipoEntradasetter(self,tipoEntrada):
            self._tipoEntrada = tipoEntrada



    def __str__(self):
        return f'Dispositivo de Entrada: {self._tipoEntrada}, Marca:{self._marca}'


if __name__ == '__main__':
    Dispo1= DispositivoEntrada('Cable', 'Samsung')

    print(Dispo1)