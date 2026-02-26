
import math
a = float(input("Ingrese A: "))
b = float(input("Ingrese B: "))
c = float(input("Ingrese C: "))

d = (b**2) - (4*a*c)

if d == 0:
    x = -b / (2 * a)
    print("X1 y X2 son iguales:", x)

elif d > 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print("X1 es:", x1)
    print("X2 es:", x2)

else:
    print("No tiene solución en los Reales")