from importador import * 



try:   
    c1 = Circulo(16)
    print(f'El area del Circulo es {c1.calcular_area()}')
    print(f'El perimetro del Circulo es {c1.calcular_perimetro()}')

    r1 = Rectangulo(16 , 16)
    print(f'El area del Rectangulo es {r1.calcular_area()}')
    print(f'El perimetro del Rectangulo es {r1.calcular_perimetro()}')

    t1 = Triangulo(16, 50)
    print(f'El area del Triangulo es {t1.calcular_area()}')
    print(f'El perimetro del Triangulo es {t1.calcular_perimetro():.{2}f}')

except TypeError as error: 
            print(f'ERROR EN EJECUCION: {error}')   


