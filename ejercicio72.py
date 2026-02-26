G = 6.67259e-11
M = 5.97e24

mayor_fuerza = None
menor_fuerza = None
suma_fuerza = 0

mayor_masa = None
suma_masa = 0

mayor_altura = None
menor_altura = None

contador = 0

while True:
    nombre = input("Nombre del satélite: ")
    masa = float(input("Masa del satélite (kg): "))
    altura = float(input("Altura del satélite (m): "))

    fuerza = (G * masa * M) / (altura ** 2)
    if mayor_fuerza is None or fuerza > mayor_fuerza:
        mayor_fuerza = fuerza
    if menor_fuerza is None or fuerza < menor_fuerza:
        menor_fuerza = fuerza

    if mayor_masa is None or masa > mayor_masa:
        mayor_masa = masa

    if mayor_altura is None or altura > mayor_altura:
        mayor_altura = altura
    if menor_altura is None or altura < menor_altura:
        menor_altura = altura

    suma_fuerza += fuerza
    suma_masa += masa
    contador += 1

    continuar = input("¿Desea ingresar otro satélite? (s/n): ")
    if continuar.lower() != "s":
        break

promedio_fuerza = suma_fuerza / contador
promedio_masa = suma_masa / contador

print("Mayor fuerza:", mayor_fuerza)
print("Menor fuerza:", menor_fuerza)
print("Promedio de fuerza:", promedio_fuerza)
print("Mayor masa:", mayor_masa)
print("Promedio de masa:", promedio_masa)
print("Mayor altura:", mayor_altura)
print("Menor altura:", menor_altura)