def calcular_raiz():
    n = float(input("Ingrese un número positivo para calcular su raíz: "))
    
    
    if n <= 0:
        print("Error: El número debe ser mayor a cero.")
    else:
        x = 0.1 
        
        while True:
 
            rn = (x + n / x) / 2
            
           
            diferencia = x - rn
            if diferencia < 0:
                diferencia = diferencia * -1
            
            if diferencia < 0.000001:
                break
            
            x = rn
            
        print("La raíz cuadrada aproximada de", n, "es:", rn)


while True:
    print(" MÉTODO DE HERÓN")
    print("1. Calcular raíz cuadrada")
    print("2. Salir")
    
    opcion = input("Elige una opción: ")

    if opcion == "1":
        calcular_raiz() 
    elif opcion == "2":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida.")