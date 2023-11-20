miarchivo = "C:/desktop/Alan.txt"

try:
    with open(miarchivo, "r") as archivo:
        contenido = archivo.read()
    print(" lo que tiene el archivo:", contenido)

except FileNotFoundError:
    print(f"Error: El archivo '{miarchivo}' no existe.")

except Exception as e:
    print(f"Error inesperado: {e}")