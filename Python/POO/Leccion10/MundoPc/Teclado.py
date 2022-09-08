from MundoPc.DispositivoEntrada import DispositivoEntrada


class Teclado(DispositivoEntrada):
    contadorTeclado = 0
    def __init__(self,tipoEntrada,marca):
        super().__init__(tipoEntrada,marca)
        Teclado.contadorTeclado +=1
        self._idTeclado = Teclado.contadorTeclado

    def __str__(self):
        return f'Teclado id: {self._idTeclado}, {super().__str__()}'


if __name__ == '__main__':
    teclado1 = Teclado('44rr','Hhh')
    print(teclado1)
    print(Teclado.contadorTeclado)