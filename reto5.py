
def calcular_nota_final(n1, n2, n3, examen):
    return (n1 * 0.25) + (n2 * 0.25) + (n3 * 0.20) + (examen * 0.30)


def capturar_notas_materia(nombre_materia):
    
    print(f"\n  > Ingresando notas de: {nombre_materia}")
    n1 = float(input("    Nota 1 (25%): "))
    n2 = float(input("    Nota 2 (25%): "))
    n3 = float(input("    Nota 3 (20%): "))
    ex = float(input("    Examen Final (30%): "))
    return calcular_nota_final(n1, n2, n3, ex)


def registrar_aprendices(cantidad):
    
    lista_estudiantes = []
    
    for i in range(1, cantidad + 1):
        print(f"\n" + "="*30)
        print(f" REGISTRO APRENDIZ {i} DE {cantidad}")
        print("="*30)
        
        nom = input("Nombre: ")
        ape = input("Apellido: ")
        eda = int(input("Edad: "))
        gen = input("Género (M/F): ")
        
       
        nota_mat = capturar_notas_materia("Matemáticas")
        nota_qui = capturar_notas_materia("Química")
        nota_fis = capturar_notas_materia("Física")
        
        
        tupla_notas = (nota_mat, nota_qui, nota_fis)
        aprendiz = (nom, ape, eda, gen, tupla_notas)
        
        lista_estudiantes.append(aprendiz)
        
    return lista_estudiantes


def mostrar_reporte(lista):
    
    if not lista:
        print("\n[!] No hay datos registrados. Por favor, registre aprendices primero.")
        return

    suma_promedios_curso = 0
    print("\n" + " " * 15 + "REPORTES FINALES")
    print("-" * 50)

    for est in lista:
        nombre, apellido, edad, genero, notas = est
        n_mat, n_qui, n_fis = notas
        
        
        promedio_estudiante = (n_mat + n_qui + n_fis) / 3
        suma_promedios_curso += promedio_estudiante
        
        print(f"Estudiante: {nombre} {apellido} ({edad} años)")
        print(f"  - Matemáticas: {n_mat:.2f}")
        print(f"  - Química:     {n_qui:.2f}")
        print(f"  - Física:      {n_fis:.2f}")
        print(f"  - PROMEDIO:    {promedio_estudiante:.2f}")
        print("-" * 30)

    promedio_general = suma_promedios_curso / len(lista)
    print("\n" + "=" * 50)
    print(f"PROMEDIO GENERAL DEL CURSO: {promedio_general:.2f}")
    print("=" * 50)


def menu():
    datos = []
    while True:
        print("\n--- SISTEMA DE GESTIÓN ACADÉMICA ---")
        print("1. Registrar 25 Aprendices")
        print("2. Ver Reporte de Notas y Promedio General")
        print("3. Salir")
        
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            
            datos = registrar_aprendices(25)
        elif opcion == "2":
            mostrar_reporte(datos)
        elif opcion == "3":
            print("Cerrando el sistema... ¡Hasta pronto!")
            break
        else:
            print("[!] Opción inválida. Intente de nuevo.")



    menu()
