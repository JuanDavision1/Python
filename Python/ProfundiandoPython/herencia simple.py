#ejemplo herencia simple
class ListaSimple:
    def __init__(self,elementos):
        self._elementos = list(elementos)

    def agregar(self,elemento):
        self._elementos.append(elemento)
    def __getitem__(self, indice):
        return self._elementos[indice]

    def ordenar(self):
        self._elementos.sort()

    def __len__(self):
        return len(self._elementos)
    def __repr__(self):
        return f'{self.__class__.__name__}{self._elementos!r}'

class listaOrdenada(ListaSimple):
    def __init__(self,elementos=[]):
        super().__init__(elementos)
        #ordenar siempre los elementos una ve inicialiados
        self.ordenar()

    def agregar(self,elemento):
        super().agregar(elemento)
        #ordenamos el nuevo elemento
        self.ordenar()
class listaenteros(ListaSimple):
    def __init__(self,elementos=[]):
        for elemento in elementos:
            self._validar(elemento)
        #una vez validados se agregan
        super().__init__(elementos)

    def _validar(self,elemento):
        #validar si es entero
        if not isinstance(elemento,int):
            raise ValueError(f'No es valor entero{elemento}')

        #sobreescribimos el metodo agregar de la clase padre
    def agregar(self,elemento):
        self._validar(elemento)
        super().agregar(elemento)

listasimple1 = ListaSimple([4,3,2,2,3])
print(listasimple1)
listaOrdenada = listaOrdenada([2,1,4,5,6])
print(listaOrdenada)
listaOrdenada.agregar(-444)
print(listaOrdenada)
print(len(listaOrdenada))
#lista de enteros
listaenteros1 = listaenteros([2,33,3,1,2,3])
print(listaenteros1)
