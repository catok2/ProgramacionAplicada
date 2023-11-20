import time

def funcion_with_time(funcion):
  def wrapper():   
    time.sleep(5)
    funcion()
  return wrapper


@funcion_with_time
def imprimo_mensaje():
  print("imprimo con retardo")


a = imprimo_mensaje()
