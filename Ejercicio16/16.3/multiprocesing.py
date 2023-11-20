import multiprocessing

def proceso_1():
    print("Proceso 1 ejecutando")

def proceso_2():
    print("Proceso 2 ejecutando")



if __name__ == "__main__":
    proceso1 = multiprocessing.Process(target=proceso_1)
    proceso2 = multiprocessing.Process(target=proceso_2)

    
    proceso1.start()
    proceso2.start()

    proceso1.join()
    proceso2.join()
