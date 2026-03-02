def clima():
    total_dias = 0
    errores = 0
    dias_validos = 0
    suma_max = 0
    suma_min = 0

    while True:
        print("\n(Ingrese 0 en ambas para terminar)")
        temp_max = float(input("Ingrese temperatura máxima: "))
        temp_min = float(input("Ingrese temperatura mínima: "))

        if temp_max == 0 and temp_min == 0:
            break
        
        total_dias += 1

        if temp_max < 14 or temp_max > 30 or temp_min < 14 or temp_min > 30:
            errores += 1
            print("Error, Temperatura fuera de rango (14-30).")
        else:
            suma_max += temp_max
            suma_min += temp_min
            dias_validos += 1

    
    if total_dias > 0:
        
        if dias_validos > 0:
            media_max = suma_max / dias_validos
            media_min = suma_min / dias_validos
        else:
            media_max = media_min = 0
            
        porcentaje_errores = (errores * 100) / total_dias
        
        print("\n--- REPORTE CLIMÁTICO ---")
        print("Número de días totales:", total_dias)
        print("Días con datos válidos:", dias_validos)
        print("Media de máximas (días válidos):", media_max)
        print("Media de mínimas (días válidos):", media_min)
        print("Cantidad de errores:", errores)
        print("Porcentaje de errores:", porcentaje_errores, "%")
    else:
        print("No se registraron datos.")


while True:
    print("SISTEMA DEL CLIMA")
    print("1. Iniciar registro de temperaturas")
    print("2. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        clima() 
    elif opcion == "2":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida.")