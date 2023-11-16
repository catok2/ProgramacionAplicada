from libreria import Libreria
from libro import *


try:
    l1 = Comics(titulo="Avengers" , autor="Stan lee", precio=2000)
    l2 = Historia(titulo="El mundo de ayer" , autor="Stefan Zweig", precio=5000)
    li = []
    li.append(l1)
    li.append(l2)
    lib = Libreria()
    print(f"El precio a pagar es de : $ {lib.calcular_precio(li)} pesos")
except TypeError as error: 
            print(f'ERROR EN EJECUCION: {error}')   
    
        






