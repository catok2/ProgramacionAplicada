class operFile:
    def __init__(self):
       pass

    def __enter__(self):
        print("se abre el archivo")
        return self
        

    def __exit__(self, type , value, traceback):
        print("se cierra el archivo")

    def write(self):
        pass    


with operFile() as file:
    file.write()
