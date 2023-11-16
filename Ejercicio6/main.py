
from importador import *



catElectronica = Categoria("Electronica")

mause = ProductoElectronica('Mause',200,10 , catElectronica)  
teclado = ProductoElectronica('Teclado',200,10 , catElectronica) 

carrito = CarritoCompra()

carrito.agregar_producto(mause)
carrito.agregar_producto(teclado)

carrito.remover_producto(mause)
cliente = Cliente("Pepe", "Perez", "94402717")

fact1 = factura(carrito, cliente)


for producto in carrito.productos:
    print(producto) 



       
       