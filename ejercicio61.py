a = int(input("Ingrese el multiplicador: "))
b = int(input("Ingrese el multiplicando: "))

resultado = 0

while a >= 1:
    if a % 2 != 0:      
        resultado += b
    a = a // 2         
    b = b * 2          

print("El resultado es:", resultado)