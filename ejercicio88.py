
codigos = [215, 102, 708]
pendientes = [10, 15, 27]
montos_unitarios = [50000, 30000, 25000]

cancelados = [0, 0, 0]
totales_pagados = [0, 0, 0]

while True:
    print("SISTEMA DEL BANCO")
    print("1. Registrar cancelación")
    print("2. Generar listado")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        
        cod_cliente = int(input("Ingrese el código del cliente: "))
        
        if cod_cliente in codigos:
            idx = codigos.index(cod_cliente) 
            
            print("El cliente tiene", pendientes[idx], "pagarés pendientes")
            cuantos = int(input("¿Cuántos pagarés va a cancelar?: "))
            
           
            if cuantos <= pendientes[idx] and cuantos > 0:
               
                pendientes[idx] -= cuantos
                cancelados[idx] += cuantos
                totales_pagados[idx] += (cuantos * montos_unitarios[idx])
                
                print("¡Pago registrado con éxito!")
            else:
                print("Error: La cantidad no es válida")
        else:
            print("Mensaje: El cliente no existe")

    elif opcion == "2":
        print("\n--- LISTADO DE CLIENTES (MAYOR A MENOR PAGO) ---")
        

        lista_final = []
        for i in range(len(codigos)):
            if cancelados[i] > 0:
                
                lista_final.append([totales_pagados[i], codigos[i], pendientes[i], cancelados[i]])
        
        
        lista_final.sort(reverse=True)
        
        
        for fila in lista_final:
            monto = fila[0]
            codigo = fila[1]
            quedan = fila[2]
            pago = fila[3]
            print("Código:", codigo, "Pendientes:", quedan, "Cancelados:", pago, "Total:", monto)

    elif opcion == "3":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida")

