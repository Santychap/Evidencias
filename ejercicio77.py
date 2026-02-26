total_pais = int(input("Ingrese el total de habitantes del país: "))

contador_estados = 0
suma_habitantes_5_estados = 0

mayor_poblacion = 0
menor_poblacion = 999999999
estado_mayor = ""
estado_menor = ""

while contador_estados < 5:
    nombre_estado = input("\nIngrese el nombre del estado: ")
    m = int(input("Ingrese la cantidad de municipios del estado: "))

    contador_municipios = 0
    suma_estado = 0

    while contador_municipios < m:
        habitantes = int(input("Habitantes del municipio: "))
        suma_estado += habitantes
        contador_municipios += 1

    print("Total habitantes del estado", nombre_estado, ":", suma_estado)

    # Comparar mayor y menor población
    if suma_estado > mayor_poblacion:
        mayor_poblacion = suma_estado
        estado_mayor = nombre_estado

    if suma_estado < menor_poblacion:
        menor_poblacion = suma_estado
        estado_menor = nombre_estado

    suma_habitantes_5_estados += suma_estado
    contador_estados += 1

# Resultados finales
porcentaje = (suma_habitantes_5_estados / total_pais) * 100
promedio = suma_habitantes_5_estados / 5

print("\nRESULTADOS:")
print("Estado con mayor población:", estado_mayor, "-", mayor_poblacion)
print("Estado con menor población:", estado_menor, "-", menor_poblacion)
print("Porcentaje respecto al país:", porcentaje, "%")
print("Promedio de habitantes por estado:", promedio)