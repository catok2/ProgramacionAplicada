def maximocumondivisor(a, b):
    if b == 0:
        return a
    else:
        return maximocumondivisor(b, a % b)

n1 = 48
n2 = 50

resultado = maximocumondivisor(n1, n2)
print(f"El maximo comun divisor de:  {n1} y {n2} es: {resultado}")