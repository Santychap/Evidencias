def bancos():
    capital = float(input("Ingrese el capital inicial a depositar: "))
    tasa = float(input("Ingrese la tasa de interés anual (ejemplo 0.06): "))
    semanas = float(input("Ingrese la duración en semanas: "))

    
    dias = int(semanas * 7) 
    contador = 0
    
    print("Calculando interés diario para", dias, "días...")

    while contador < dias:
        
        interes_diario = (tasa * capital) / 365
        capital = capital + interes_diario
        contador = contador + 1
    
    
    print("El capital total acumulado es:", round(capital, 2))


while True:
    print("SISTEMA DE BANCOS")
    print("1. Calcular capital acumulado")
    print("2. Salir")
    
    opcion = input("Elige una opción: ")

    if opcion == "1":
        bancos() 
    elif opcion == "2":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida.")