def suma_digitos(numero):
    if numero % 2 == 0:
        print(numero)
        return sum(int(digito) for digito in str(numero))
    else:
        print(numero)
        return max(numero - 3, 0) + 1


numero_ejemplo = 10
resultado = suma_digitos(numero_ejemplo)
print(f"Resultado para el número {numero_ejemplo}: {resultado}")