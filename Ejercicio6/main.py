
from importador import *


mause = Producto('Mause', 200, 10 )  
teclado = Producto('Teclado',200,10 ) 

carrito = CarritoCompra()

carrito.agregar_producto(mause)
carrito.agregar_producto(teclado)

# carrito.remover_producto(mause)
cliente = Cliente("Pepe", "Perez", "94402717")
cliente.add_carrito(carrito)
fact1 = factura(cliente)





print(fact1.totFactura) 
# for producto in carrito.productos:
#     print(producto) 



       
       