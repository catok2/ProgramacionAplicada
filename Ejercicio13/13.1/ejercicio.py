def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def suma_primos_hasta(num):
    suma = 0
    for i in range(2, num + 1):
        if es_primo(i):
            suma += i
    return suma

numero_deseado = 12
resultado = suma_primos_hasta(numero_deseado)
print(f"La suma de los números primos hasta {numero_deseado} es: {resultado}")