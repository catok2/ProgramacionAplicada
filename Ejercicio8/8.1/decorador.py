def funcion_registro_and_devolucion(funcion):
  def wrapper(*args):
    print(f"Se envia estos argumentos {args} y la funcion :  {funcion.__name__}")
    result = funcion(*args)
    print(f"devolvio {result}")
    return result
  return wrapper


@funcion_registro_and_devolucion
def imprimo(a, b):
  return a + b



a = imprimo(2, 3)