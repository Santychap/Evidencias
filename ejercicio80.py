def senso():
    personas = []
    
    estado_codigo = input("Ingrese el código del Estado: ")
    ciudad_codigo = input("Ingrese el código de la Ciudad: ")
    municipio_codigo = input("Ingrese el código del Municipio: ")

    while True:
        edad = int(input("\nIngrese la edad (o -1 para terminar este municipio): "))
        if edad == -1:
            break
        
        nivel_educacion = input("Nivel de educación (N: Ninguno, B: Básico, S: Superior, P: Postgrado): ").upper()
        situacion_actual = input("Situación actual (D: Desempleado, E: Empleado): ").upper()
        
        persona = (edad, nivel_educacion, situacion_actual)
        personas.append(persona)

    contador = 0
    for p in personas:
        e, n, s = p 
        if s == 'D' and n == 'N' and e > 25:
            contador += 1
            
    print(f"\n>>> RESULTADO: Ciudad {ciudad_codigo}, Municipio {municipio_codigo}")
    print(f"Personas desempleadas, sin educación y > 25 años: {contador}")


while True:
    print("\n--- SISTEMA DE CENSO ---")
    print("1. Iniciar registro de censo")
    print("2. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        senso() 
    elif opcion == "2":
        print("¡Saliendo del sistema! Hasta luego.")
        break  
    else:
        print("Opción no válida.")