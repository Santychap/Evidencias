
opcion = "s"
while opcion == "s":
    edad = int(input("Edad: "))
    sexo = input("Sexo (h/m): ")
    estado_civil = input("Estado civil (soltero/casado/divorciado): ")
    especialidad = input("Especialidad: ")

    if sexo =="m":
        promedio_mujeres += edad
        cantidad_mujeres += 1
    elif sexo =="h":
        promedio_hombres += edad
        cantidad_hombres += 1

    if estado_civil == "soltero":
        cantidad_solteros += 1
    elif estado_civil == "casado":
        cantidad_casados += 1
    elif estado_civil == "divorciado":
        cantidad_divorciados += 1

    if especialidad in especialidad:
        especialidad[especialidad] += 1
    else:
        especialidad[especialidad] = 1

    if sexo == "m" and edad > 21:
        mujeres_adultas += 1
    elif sexo == "h" and edad < 21 and edad > 17:
        hombres_jovenes += 1

    opcion = input("¿Desea ingresar otro alumno? (s/n): ")