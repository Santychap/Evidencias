def satelites():
    G = 6.67259e-11
    M_TIERRA = 5.97e24

    mayor_fuerza = 0
    menor_fuerza = 0
    suma_fuerza = 0
    
    mayor_masa = 0
    suma_masa = 0
    
    mayor_altura = 0
    menor_altura = 0
    
    contador = 0

    while True:
        print("REGISTRO DE SATÉLITE")
        nombre = input("Nombre del satélite (o 'fin' para terminar): ")
        if nombre.lower() == "fin":
            break
            
        pais = input("País: ")
        masa = float(input("Masa del satélite (Kg): "))
        r = float(input("Distancia/Altura (Mts): "))

        fuerza = (G * masa * M_TIERRA) / (r ** 2)

        if contador == 0:
            mayor_fuerza = menor_fuerza = fuerza
            mayor_masa = masa
            mayor_altura = menor_altura = r
        else:
            
            if fuerza > mayor_fuerza: mayor_fuerza = fuerza
            if fuerza < menor_fuerza: menor_fuerza = fuerza
            if masa > mayor_masa: mayor_masa = masa
            if r > mayor_altura: mayor_altura = r
            if r < menor_altura: menor_altura = r

       
        suma_fuerza = suma_fuerza + fuerza
        suma_masa = suma_masa + masa
        contador = contador + 1

        print("Fuerza de atracción calculada:", fuerza, "N")

    if contador > 0:
        
        promedio_fuerza = suma_fuerza / contador
        promedio_masa = suma_masa / contador

        print("INFORME FINAL NASA ")
        print("a) Mayor fuerza de atracción:", mayor_fuerza, "N")
        print("   Menor fuerza de atracción:", menor_fuerza, "N")
        print("b) Fuerza de atracción promedio:", promedio_fuerza, "N")
        print("c) Mayor masa de los satélites:", mayor_masa, "Kg")
        print("d) Masa promedio de los satélites:", promedio_masa, "Kg")
        print("e) Mayor altura registrada:", mayor_altura, "Mts")
        print("   Menor altura registrada:", menor_altura, "Mts")
      
    else:
        print("\nNo se ingresaron datos.")

while True:
    print("\n--- SISTEMA GRAVITATORIO NASA ---")
    print("1. Procesar muestra de satélites")
    print("2. Salir")

    opcion = input("Seleccione opción: ")

    if opcion == "1":
        satelites()
    elif opcion == "2":
        print("Programa finalizado.")
        break
    else:
        print("Opción no válida.")