

def colegio():
    g = int(input("Ingrese la cantidad de grupos: "))

    contador_grupos = 0
    suma_promedios_grupos = 0

    while contador_grupos < g:
        print("\nGRUPO", contador_grupos + 1)
        n = int(input("Ingrese la cantidad de alumnos del grupo: "))

        contador_alumnos = 0
        suma_promedios_alumnos = 0

        while contador_alumnos < n:
            print("\n Alumno", contador_alumnos + 1)
            m = int(input("Ingrese la cantidad de materias: "))

            contador_materias = 0
            suma_materias = 0

            while contador_materias < m:
                print("  Materia", contador_materias + 1)

                nota1 = float(input("   Nota 1: "))
                nota2 = float(input("   Nota 2: "))
                nota3 = float(input("   Nota 3: "))

                promedio_materia = (nota1 + nota2 + nota3) / 3
                suma_materias += promedio_materia

                contador_materias += 1

            promedio_alumno = suma_materias / m
            print("   Promedio del alumno:", promedio_alumno)

            suma_promedios_alumnos += promedio_alumno
            contador_alumnos += 1

        promedio_grupo = suma_promedios_alumnos / n
        print("\nPromedio del grupo:", promedio_grupo)

        suma_promedios_grupos += promedio_grupo
        contador_grupos += 1

    promedio_general = suma_promedios_grupos / g
    print("\nPromedio general de todos los grupos:", promedio_general)

while True:
    print("\n--- SISTEMA DE COLEGIO ---")
    print("1. Iniciar promedios")
    print("2. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        colegio() 
    elif opcion == "2":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Intente de nuevo.")
