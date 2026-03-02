
def grados():
    F = int(input("Ingrese el valor de F (grados Fahrenheit): "))
    C = 5 * (F - 32) / 9
    R = F + 459.67
    K = C + 273.15  

    print("Fahrenheit\tCelsius\tRankine\tKelvin")
    print(f"{F}\t\t{C:.2f}\t\t{R:.2f}\t{K:.2f}")

while True:
    print("\n--- MENÚ DE GRADOS ---")
    print("1. Ejecutar conversión de grados")
    print("2. Salir")
    
    opcion = input("Elige una opción: ")

    if opcion == "1":

        F = int(input("Ingrese el valor de F (grados Fahrenheit): "))
        C = 5 * (F - 32) / 9
        R = F + 459.67
        K = C + 273.15  

        print("Fahrenheit\tCelsius\tRankine\tKelvin")
        print(f"{F}\t\t{C:.2f}\t\t{R:.2f}\t{K:.2f}")
    elif opcion == "2":
        print("Saliendo del menú...")
        break  
        
    else:
        print("Opción no válida, intenta de nuevo.")






