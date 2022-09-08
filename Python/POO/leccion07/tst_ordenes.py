from Orden import Orden
from producto import producto

if __name__ == '__main__':
    producto1 = producto('camisa', 10000)
    producto2 = producto('Pantalon', 3000)
    producto3 = producto('Cadena', 4.00)
    producto4 = producto('Pulsera', 23000)
    productos1=[producto1,producto2]
    productos2 = [producto3, producto3]
    orden1= Orden(productos1)
    orden1.agregarProducto(producto3)
    orden1.agregarProducto(producto4)
    orden2 = Orden(productos2)
    print(orden1)
    print(f'total:{orden1.sumaprecios()}')
    print(orden2)
    print(f'total:{orden2.sumaprecios()}')