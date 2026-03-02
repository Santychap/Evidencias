
def calcular_suma_pares():
    suma = 0
    for i in range(97, 1004):
        if i % 2 == 0:
            suma += i
    print("suma", suma)

while True:
    print("\n--- MENÚ DE SUMA ---")
    print("1. Ejecutar ejercicio: suma de números pares entre 97 y 1004")
    print("2. Salir")
    
    opcion = input("Elige una opción: ")

    if opcion == "1":
        calcular_suma_pares()
    elif opcion == "2":
        print("Saliendo del menú...")
        break
    else:
        print("Opción no válida, intenta de nuevo.")
