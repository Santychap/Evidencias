
valor1 = float(input("Ingrese el numero entero A: "))
valor2 = float(input("Ingrese el numero entero B: "))
valor3 = float(input("Ingrese el numero entero C: "))

area_triangulo = (valor1 * valor2) / 2
area_rectangulo = valor1 * valor2
area_circulo = valor2 * (valor1 ** 2)

if area_triangulo == valor3:
    print("Corresponde a un TRIÁNGULO")
elif area_circulo == valor3:
    print("Corresponde a un CÍRCULO")
elif area_rectangulo == valor3:
    print("Corresponde a un RECTÁNGULO")
else:
    print("No corresponde a ninguna figura conocida")
