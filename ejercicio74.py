def bloquera():
    
    limite = int(input("Ingrese el número de bloques que debe producir cada obrero en la semana: "))

    contador_obreros = 0
    suma_total_bloquera = 0
    obreros_cumplen = 0
    mayor_produccion = 0
    nombre_mayor = ""

    op = "s"
    while op == "s" or op == "S":
        nombre = input("\nNombre del obrero: ")
        contador_dias = 0
        total_semana = 0

        
        while contador_dias < 6: 
            print("Día", contador_dias + 1)
            produccion_dia = int(input("Bloques producidos hoy: "))
            total_semana = total_semana + produccion_dia
            contador_dias = contador_dias + 1

        porcentaje = (total_semana / limite) * 100

        print("\n--- REPORTE INDIVIDUAL ---")
        print("OBRERO:", nombre)
        print("Total producido en la semana:", total_semana)
        print("Porcentaje respecto al límite:", porcentaje, "%")
        if total_semana >= limite:
            obreros_cumplen = obreros_cumplen + 1

        if total_semana > mayor_produccion:
            mayor_produccion = total_semana
            nombre_mayor = nombre

        suma_total_bloquera = suma_total_bloquera + total_semana
        contador_obreros = contador_obreros + 1

        op = input("\n¿Desea ingresar otro obrero? (s/n): ")

    if contador_obreros > 0:
        porcentaje_cumplen = (obreros_cumplen / contador_obreros) * 100
        promedio_bloquera = suma_total_bloquera / contador_obreros

        print("\n=== RESULTADOS GENERALES DE LA SEMANA ===")
        print("Total de obreros procesados:", contador_obreros)
        print("Porcentaje de obreros que cumplieron la meta:", porcentaje_cumplen, "%")
        print("El mejor productor fue:", nombre_mayor, "con", mayor_produccion, "bloques")
        print("Promedio de producción de la empresa:", promedio_bloquera)
    else:
        print("\nNo se registraron datos de obreros.")


while True:
    print("SISTEMA DE LA BLOQUERA")
    print("1. Iniciar registro semanal")
    print("2. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        bloquera() 
    elif opcion == "2":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Intente de nuevo.")
