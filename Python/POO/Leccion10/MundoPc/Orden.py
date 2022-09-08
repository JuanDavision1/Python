class Orden:
    contadorOrdenes = 0
    def __init__(self,ListaCompu):
        Orden.contadorOrdenes +=1
        self._idOrden = Orden.contadorOrdenes
        self._ListaCompu = ListaCompu

    def agregar_compu(self,computadora):
        self._ListaCompu.append(computadora)

    def __str__(self):
        computadoras_str =''
        for computadora in self._ListaCompu:
            computadoras_str += computadora.__str__()

        return f'''
        Orden : {self._idOrden}
        Computadoras : {computadoras_str}
        '''
