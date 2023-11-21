
nombre_archivo = "C\DESKTOP\ALAN3.txt"
salida_archivo = "C\DESKTOP\ALAN3.txt"

try:
   
    with open(nombre_archivo, "r") as nombre_archivo, open(salida_archivo, "w") as salida_archivo:
        contenido = nombre_archivo.read()
        salida_archivo.write(contenido)
    print("Contenido copiado exitosamente.")

except FileNotFoundError:
    print(f"Error: El archivo de entrada '{nombre_archivo}' no existe.")
except Exception as e:
    print(f"Error inesperado: {e}")