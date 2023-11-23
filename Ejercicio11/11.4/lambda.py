import math

list_numeros = [2, 4,8, 16]

raises_numeros = list(map(lambda x: math.sqrt(x), list_numeros))

print(raises_numeros)