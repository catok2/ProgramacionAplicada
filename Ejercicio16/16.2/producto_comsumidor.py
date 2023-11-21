import threading
import queue
import time
import random


cola = queue.Queue(maxsize=5)  


def productor():
    for i in range(10):
        dato = f"Dato-{i}"
        cola.put(dato)
        print(f"Productor produce: {dato}")
        time.sleep(random.uniform(0.1, 0.5))

def consumidor():
    while True:
        dato = cola.get()
        print(f"Consumidor consume: {dato}")
        time.sleep(random.uniform(0.1, 0.5))
        cola.task_done()


hilo_productor = threading.Thread(target=productor)
hilo_consumidor = threading.Thread(target=consumidor)

hilo_productor.start()
hilo_consumidor.start()

hilo_productor.join()
hilo_consumidor.join()