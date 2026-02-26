
nombres = []
sexos = []
edades = []
suma_edades = 0
profesor_mas_joven = ""
profesor_mas_viejo = ""
edad_mas_joven = 100
edad_mas_vieja = 0

contador_profesoras_mayores_promedio = 0
contador_profesores_menores_promedio = 0

promedio_edad = 0

num_profesores = int(input("Ingrese el número de profesores: "))

for i in range(num_profesores):
    nombre = input("Ingrese el nombre del profesor: ")
    sexo = input("Ingrese el sexo del profesor (M/F): ")
    edad = int(input("Ingrese la edad del profesor: "))

    nombres.append(nombre)
    sexos.append(sexo)
    edades.append(edad)

    suma_edades += edad

    if edad < edad_mas_joven:
        edad_mas_joven = edad
        profesor_mas_joven = nombre

    if edad > edad_mas_vieja:
        edad_mas_vieja = edad
        profesor_mas_viejo = nombre

promedio_edad = suma_edades / num_profesores

for i in range(num_profesores):
    if sexos[i] == "F" and edades[i] > promedio_edad:
        contador_profesoras_mayores_promedio += 1
for i in range(num_profesores):
    if edades[i] < promedio_edad:
        contador_profesores_menores_promedio += 1
print("Edad promedio del grupo de profesores:", promedio_edad)
print("Nombre del profesor más joven del grupo:", profesor_mas_joven)
print("Nombre del profesor con más edad:", profesor_mas_viejo)
print("Número de profesoras con edad mayor al promedio:", contador_profesoras_mayores_promedio)
print("Número de profesores con edad menor al promedio:", contador_profesores_menores_promedio)