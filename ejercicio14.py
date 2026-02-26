
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))
d = float(input("Ingrese el valor de d: "))
e = float(input("Ingrese el valor de e: "))
f = float(input("Ingrese el valor de f: "))


denominador = (a * e) - (b * d)

x = ((c * e) - (b * f)) / denominador
y = ((a * f) - (c * d)) / denominador

print("El valor de X es:", x)
print("El valor de Y es:", y)

