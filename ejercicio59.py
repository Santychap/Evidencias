alumnos = ["Juan", "Melisa", "Manuela", "Gabi", "Gabriel", "Elías"]

menor_programacion = None
cont_no_presentaron_ingles = 0
cont_presentaron_ingles = 0
cont_aprobaron_todo = 0
suma_programacion = 0
cont_alumnos = 0
cont_presentaron_mate = 0
cont_reprobaron_mate = 0

opcion = "s"

while opcion == "s":
    matematica = float(input("Nota de Matemática (0 si no presentó): "))
    programacion = float(input("Nota de Programación: "))
    ingles = float(input("Nota de Inglés (0 si no presentó): "))

    cont_alumnos += 1

    # a) menor nota de programación
    if menor_programacion is None or programacion < menor_programacion:
        menor_programacion = programacion

    # b) no presentaron inglés vs sí presentaron
    if ingles == 0:
        cont_no_presentaron_ingles += 1
    else:
        cont_presentaron_ingles += 1

    # c) aprobaron todas
    if matematica >= 3 and programacion >= 3 and ingles >= 3:
        cont_aprobaron_todo += 1


    suma_programacion += programacion


    if matematica > 0:
        cont_presentaron_mate += 1
        if matematica < 3:
            cont_reprobaron_mate += 1

    opcion = input("¿Desea ingresar otro alumno? (s/n): ")


promedio_programacion = suma_programacion / cont_alumnos

if cont_presentaron_ingles > 0:
    porcentaje_no_ingles = (cont_no_presentaron_ingles / cont_presentaron_ingles) * 100
else:
    porcentaje_no_ingles = 0

if cont_presentaron_mate > 0:
    porcentaje_reprobaron_mate = (cont_reprobaron_mate / cont_presentaron_mate) * 100
else:
    porcentaje_reprobaron_mate = 0

print("\nRESULTADOS:")
print("a) Nota menor en Programación:", menor_programacion)
print("b) % que no presentaron Inglés:", porcentaje_no_ingles)
print("c) Alumnos que aprobaron todas:", cont_aprobaron_todo)
print("d) Promedio general en Programación:", promedio_programacion)
print("e) % que reprobaron Matemática:", porcentaje_reprobaron_mate)