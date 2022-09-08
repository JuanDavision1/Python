from MundoPc.DispositivoEntrada import DispositivoEntrada


class raton(DispositivoEntrada):
    contadorRatones =0
    def __init__(self,tipoEntrada,marca):
        super().__init__(tipoEntrada,marca)
        raton.contadorRatones += 1
        self._idRaton = raton.contadorRatones

    def __str__(self):
        return f'Raton: Id del Raton: {self._idRaton}, {super().__str__()}'

if __name__ == '__main__':
    raton1 = raton('mause','Apple')
    raton2 = raton('ff','Apple')
    print(raton.contadorRatones)