
import math
a = int(input("Ingrese el lado A: "))
b = int(input("Ingrese el lado B: "))
c = int(input("Ingrese el lado C: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    print("Los datos corresponden a un triángulo.")

    if a == b == c:
        tipo = "Equilátero"
    elif a == b or a == c or b == c:
        tipo = "Isósceles"
    else:
        tipo = "Escaleno"
    
    print(f"El triángulo es: {tipo}")
  
    s = (a + b + c) / 2 
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    
    print("El área del triángulo es:", area)

else:
    print("Los datos NO corresponden a un triángulo.")


