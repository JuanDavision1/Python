class padre:
    def __init__(self):
        print('inicializados Padre')

    def metodo(self):
        print('Mensaje metodo padre')

class hija(padre):
    # se manda a llamar el metodo init de la clase padre
    #siempre y cuando la clase hija no defina su propio metodo init

    def __init__(self):
        #se puede llamar el metodo init de la clase padre
        super().__init__()
        print('inicializador hija')

    #sobreescrbimos el metodo de la clase padre
    def metodo(self):
        print('Metodo sobreescrita en la clase hija')
        super().metodo()


#padre = padre()
#padre.metodo()
hijo1 = hija()
hijo1.metodo()