def promedio_peso():
    
    suma_niños = suma_adolescentes = suma_adultos = suma_viejos = 0
    cant_niños = cant_adolescentes = cant_adultos = cant_viejos = 0

    print("\n--- Registro de Pesos (10 personas para el ejemplo) ---")
    for i in range(10):
        print(f"\nPersona {i+1}:")
        edad = int(input("Ingrese la edad: "))
        peso = float(input("Ingrese el peso (kg): "))

        if 0 <= edad <= 12:
            suma_niños += peso
            cant_niños += 1
        elif 13 <= edad <= 29:
            suma_adolescentes += peso
            cant_adolescentes += 1
        elif 30 <= edad <= 59:
            suma_adultos += peso
            cant_adultos += 1
        elif edad >= 60:
            suma_viejos += peso
            cant_viejos += 1
    prom_niños = suma_niños / cant_niños if cant_niños > 0 else 0
    prom_adol = suma_adolescentes / cant_adolescentes if cant_adolescentes > 0 else 0
    prom_adultos = suma_adultos / cant_adultos if cant_adultos > 0 else 0
    prom_viejos = suma_viejos / cant_viejos if cant_viejos > 0 else 0

    
    print("\n" + "="*30)
    print(f"Promedio Niños: {prom_niños:.2f} kg")
    print(f"Promedio Jóvenes: {prom_adol:.2f} kg")
    print(f"Promedio Adultos: {prom_adultos:.2f} kg")
    print(f"Promedio Viejos: {prom_viejos:.2f} kg")
    print("="*30)


while True:
    print("\n--- MENÚ DE ESTADÍSTICAS ---")
    print("1. Ejecutar promedios de peso")
    print("2. Salir")
    
    opcion = input("Elige una opción: ")

    if opcion == "1":
        promedio_peso() 
    elif opcion == "2":
        print("Saliendo del menú... ¡Adiós!")
        break
    else:
        print("Opción no válida, intenta de nuevo.")

