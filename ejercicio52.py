
peso =0
suma_niños=0
suma_adolcentes=0
suma_adultos=0
suma_viejos=0
cantidad_niños=0
cantidad_adolcentes=0
cantidad_adultos=0
cantidad_viejos=0

for i in range(100):
    edad = int(input("Ingrese la edad de la persona: "))
    peso = float(input("Ingrese el peso de la persona: "))

    if edad >= 0 and edad <= 12:
        suma_niños += peso
        cantidad_niños += 1
    elif edad >= 13 and edad <= 29:
        suma_adolcentes += peso
        cantidad_adolcentes += 1
    elif edad >= 30 and edad <= 59:
        suma_adultos += peso
        cantidad_adultos += 1
    elif edad >= 60:
        suma_viejos += peso
        cantidad_viejos += 1
promedio_niños = suma_niños / cantidad_niños if cantidad_niños > 0 else 0
promedio_adolcentes = suma_adolcentes / cantidad_adolcentes if cantidad_adolcentes > 0 else 0
promedio_adultos = suma_adultos / cantidad_adultos if cantidad_adultos > 0 else 0
promedio_viejos = suma_viejos / cantidad_viejos if cantidad_viejos > 0 else 0
print("El promedio de peso de los niños es: ", promedio_niños)
print("El promedio de peso de los jóvenes es: ", promedio_adolcentes)
print("El promedio de peso de los adultos es: ", promedio_adultos)
print("El promedio de peso de los viejos es: ", promedio_viejos)


