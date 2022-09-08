class producto:
    contador_poductos =0
    def __init__(self,nombre, precio):
        producto.contador_poductos +=1
        self._id_producto = producto.contador_poductos
        self._nombre=nombre
        self._precio =precio

    @property
    def precio(self):
        return self._precio

        #str esrepreseentacion del obj en string
    def __str__(self):
        return f'Id :{self._id_producto}, nombre {self._nombre} precio {self._precio}'

if __name__ == '__main__':
    producto1 = producto('camisa' ,10000)
    print(producto1)
    producto2 = producto('Pantalon', 3000)
    print(producto2)
