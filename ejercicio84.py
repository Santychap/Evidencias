
proveedores = ["Zapateria Real", "Abastos Gomez", "Cómputos Express"]
ciudades = ["Valencia", "Caracas", "Maracay"]
articulos = [150, 45, 200]

datos_unidos = list(zip(proveedores, ciudades, articulos))
datos_unidos.sort() 
proveedores, ciudades, articulos = map(list, zip(*datos_unidos))

def menu():
    while True:
        print("\n" + "="*30)
        print(f"LISTADO ORDENADO: {proveedores}")
        print("="*30)
        print("a. Consultar proveedor")
        print("b. Actualizar ciudad")
        print("c. Actualizar artículos")
        print("d. Salir")
        
        opcion = input("\nSeleccione una opción: ").lower()
        
        if opcion == 'd':
            print("Programa finalizado.")
            break
            
        if opcion in ['a', 'b', 'c']:
            nombre = input("Nombre del proveedor a buscar: ")
            
            # Búsqueda del índice (Posición en el vector)
            if nombre in proveedores:
                idx = proveedores.index(nombre)
                
                if opcion == 'a':
                    print(f"-> Proveedor: {proveedores[idx]}")
                    print(f"-> Ciudad: {ciudades[idx]}")
                    print(f"-> Artículos: {articulos[idx]}")
                
                elif opcion == 'b':
                    nueva_ciu = input(f"Ingrese nueva ciudad para {nombre}: ")
                    ciudades[idx] = nueva_ciu
                    print("¡Ciudad actualizada con éxito!")
                    
                elif opcion == 'c':
                    try:
                        nuevo_stock = int(input(f"Nuevo número de artículos para {nombre}: "))
                        articulos[idx] = nuevo_stock
                        print("¡Cantidad actualizada!")
                    except ValueError:
                        print("Error: Debe ingresar un número entero.")
            else:
                print("Error: El proveedor no existe en el registro.")
        else:
            print("Opción no válida.")

menu()

