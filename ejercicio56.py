
dividendo = int(input("Ingrese el dividendo: "))
divisor = int(input("Ingrese el divisor: "))
cociente = 0
resto = dividendo

while resto >= divisor:
    resto -= divisor
    cociente +=1
print("El cociente es: ", cociente)
print("El resto es: ", resto)