from producto import producto


class Orden:
    contador_ordenes = 0

    def __init__(self ,productos):
        Orden.contador_ordenes +=1
        self._id_orden = Orden.contador_ordenes
        #conversion a lista para restringirlo a que sea solo esop
        self._productos = list(productos)


    def agregarProducto(self,producto):
        #agregar al final un producto
        self._productos.append(producto)


    def sumaprecios(self):
        total =0
        for producto in self._productos:
            #recuperar el precio
            total += producto.precio
            return total


    def __str__(self):
        productos_str =''
        for producto in self._productos:
            productos_str += producto.__str__() + '|'

        return f'Orden:{self._id_orden},\n Productos:{productos_str}'

if __name__ == '__main__':
    producto1 = producto('camisa', 10000)

    producto2 = producto('Pantalon', 3000)
    productos1=[producto1,producto2]
    orden1= Orden(productos1)
    orden2 = Orden(productos1)
    print(orden1)
    print(orden2)
