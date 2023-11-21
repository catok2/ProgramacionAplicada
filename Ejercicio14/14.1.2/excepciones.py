
lista_numeros = [1, 2, 3, 4, 5]

try:

    indice_delnumero = 1
    elemento = lista_numeros[indice_delnumero]
    print(f"Elemento en el índice es : {elemento}")

except IndexError:
    print("Fuera de rango")

except ValueError:
    print("valido el tipo ingresado")

except Exception as e:
    print(f"error: {e}")