

alumnos = [
    {"nombre": "María", "notas": [16, 14, 15, 13, 9]},
    {"nombre": "Juan Carlos", "notas": [10, 9, 7, 11, 14]},
    {"nombre": "Josefina", "notas": [13, 12, 15, 17, 13]},
    {"nombre": "José Luis", "notas": [7, 11, 10, 8, 17]}
]

promedios_individuales = []
print(f"{'Número':<8} {'Nombre':<15} {'Promedio'}")

for i, alumno in enumerate(alumnos, 1):
    promedio_ind = sum(alumno["notas"]) / len(alumno["notas"])
    promedios_individuales.append(promedio_ind)
    print(f"{i:<8} {alumno['nombre']:<15} {promedio_ind:.1f}")

promedio_clase = sum(promedios_individuales) / len(promedios_individuales)

menores = sum(1 for p in promedios_individuales if p < promedio_clase)
mayores = sum(1 for p in promedios_individuales if p > promedio_clase)

print("-" * 40)
print("Promedio de la clase:", promedio_clase)
print("Alumnos con definitiva menor al promedio: ", menores)
print("Alumnos con definitiva mayor al promedio: ", mayores)
