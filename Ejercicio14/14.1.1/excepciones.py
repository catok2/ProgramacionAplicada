try:
    numerador = float(input("Ingrese el primer numero: "))
    denominador = float(input("Ingrese el segundo numero: ")) 
    resultado = numerador / denominador
    print(f"Resultado de la división: {resultado}")

except ZeroDivisionError:
    print("Error: estas intentnado dividir por 0")

except ValueError:
    print("Error: los numeros ingresados no son validos.")

except Exception as e:
    print(f"Error : {e}")