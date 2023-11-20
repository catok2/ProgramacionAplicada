def funcion_registro_and_devolucion(funcion):
  def wrapper( a , b):
    if isinstance(a, int ) and isinstance(b,int):
        print(f"los valores son correctos de tipo int , nombre de  la funcion :  {funcion.__name__}")
        result = funcion(a , b)
    print(f"devolvio {result}")
    return result
  return wrapper


@funcion_registro_and_devolucion
def imprimo(a, b):
  return a + b



a = imprimo(2, 3)