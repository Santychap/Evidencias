limite = int(input("Ingrese el número de bloques que debe producir cada obrero en la semana: "))

contador_obreros = 0
suma_total_bloquera = 0
obreros_cumplen = 0

mayor_produccion = 0
nombre_mayor = ""

op = "s"
while op == "s":
    nombre = input("\nNombre del obrero: ")

    contador_dias = 0
    total_semana = 0

    while contador_dias < 6:  # suponiendo 6 días de trabajo (lunes a sábado)
        produccion_dia = int(input("Bloques producidos hoy: "))
        total_semana += produccion_dia
        contador_dias += 1

    porcentaje = (total_semana / limite) * 100

    print("\nOBRERO:", nombre)
    print("Total producido en la semana:", total_semana)
    print("Porcentaje respecto al límite:", porcentaje, "%")

    # Obreros que alcanzan o superan el límite
    if total_semana >= limite:
        obreros_cumplen += 1

    # Buscar el que más produjo
    if total_semana > mayor_produccion:
        mayor_produccion = total_semana
        nombre_mayor = nombre

    suma_total_bloquera += total_semana
    contador_obreros += 1

    op = input("\n¿Desea ingresar otro obrero? (s/n): ")

# Resultados generales
porcentaje_cumplen = (obreros_cumplen / contador_obreros) * 100
promedio_bloquera = suma_total_bloquera / contador_obreros

print("\nRESULTADOS GENERALES")
print("Porcentaje de obreros que cumplieron o superaron el límite:", porcentaje_cumplen, "%")
print("Obrero que más produjo:", nombre_mayor, "con", mayor_produccion, "bloques")
print("Promedio de producción semanal de la bloquera:", promedio_bloquera)