def numero(K, N):
    if N > K:
        for i in range(N, K - 1, -1):
            print(i)
    else:
        print("Error: N debe ser mayor que K para la cuenta regresiva.")

while True:
    print("\n--- MENÚ DE NÚMEROS ---")
    print("1. Ejecutar cuenta regresiva")
    print("2. Salir")
    
    opcion = input("Elige una opción: ")

    if opcion == "1":

        K = int(input("Ingrese el valor de K (fin): "))
        N = int(input("Ingrese el valor de N (inicio): "))
        
        print(f"\nResultado de la cuenta de {N} a {K}:")
        numero(K, N)
        
    elif opcion == "2":
        print("Saliendo del menú...")
        break  
        
    else:
        print("Opción no válida, intenta de nuevo.")



