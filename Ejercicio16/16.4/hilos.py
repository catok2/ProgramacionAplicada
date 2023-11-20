import threading
import time

def primer_funcion():
    for _ in range(5):
        print("Función 1 ejecutándose")
        time.sleep(1)

def segunda_funcion():
    for _ in range(5):
        print("Función 2 ejecutándose")
        time.sleep(1)


hilo_1 = threading.Thread(target=primer_funcion)
hilo_2 = threading.Thread(target=segunda_funcion)


hilo_1.start()
hilo_2.start()

print("Ambos hilos han terminado.")