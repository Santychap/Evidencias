N = float(input("Ingrese un número positivo: "))

while N <= 0:
    N = float(input("Error. Ingrese un número positivo: "))

X = 0.1
RN = (X + N / X) / 2

while abs(X - RN) >= 0.000001:
    X = RN
    RN = (X + N / X) / 2

print("La raíz aproximada es:", RN)
    

