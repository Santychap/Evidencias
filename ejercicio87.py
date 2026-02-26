
nombres_espectaculos = []
ingresos = []
asistentes = [] 
gastos = []
num_espectaculos = int(input("Ingrese el número de espectáculos: "))

for i in range(num_espectaculos):
    nombre = input("Ingrese el nombre del espectáculo: ")
    ingreso = float(input("Ingrese el total de ingresos en Bolívares: "))
    asistente = int(input("Ingrese la cantidad de asistentes: "))
    gasto = float(input("Ingrese el total de gastos: "))

    nombres_espectaculos.append(nombre)
    ingresos.append(ingreso)
    asistentes.append(asistente)
    gastos.append(gasto)

for i in range(num_espectaculos):
    if ingresos[i] < gastos[i]:
        print("El espectáculo", nombres_espectaculos[i], "generó pérdidas.")
mayor_ganancia = ingresos[0] - gastos[0]
espectaculo_mayor_ganancia = nombres_espectaculos[0]

for i in range(num_espectaculos):
    if ingresos[i] - gastos[i] > mayor_ganancia:
        mayor_ganancia = ingresos[i] - gastos[i]
        espectaculo_mayor_ganancia = nombres_espectaculos[i]

print("El espectáculo con mayor ganancia fue:", espectaculo_mayor_ganancia) 