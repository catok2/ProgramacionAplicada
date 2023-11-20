import os

class cambiarDirectorio:
    def __init__(self, directorio):
        self.nuevo_directo  = directorio
        self.directorio_original = os.getcwd()

    def __enter__(self):
        os.chdir(self.nuevo_directo)
        print(f"cambie el directorio a: {os.getcwd()}")

    def __exit__(self, type, value, traceback):
        os.chdir(self.directorio_original)
        print(f"Vuelvo al directorio original: {os.getcwd()}")

with cambiarDirectorio("/C:/desktop/Alan_practica/directorio"):
    pass
