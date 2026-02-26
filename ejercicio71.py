
total_huerfanos = 0
huerfanos_tachira = 0
huerfanos_distrito_capital = 0
grupo1 = 0
grupo2 = 0
grupo3 = 0
grupo4 = 0
huerfanos_ninos = 0
huerfanos_ninas = 0

while True:
    sexo = input("Ingrese el sexo (h/m): ")
    edad = int(input("Ingrese la edad: "))
    nombre_orfanato = input("Nombre del orfanato: ")
    estado = input("Estado donde está el orfanato: ")

    if edad < 1:
        grupo1 += 1
    elif edad >= 1 and edad <= 3:
        grupo2 += 1
    elif edad >= 4 and edad <= 6:
        grupo3 += 1
    else:
        grupo4 += 1

    if sexo == "h":
        huerfanos_ninos += 1
    else:
        huerfanos_ninas += 1

    if estado.lower() == "tachira":
        huerfanos_tachira += 1
    elif estado.lower() == "distrito capital":
        huerfanos_distrito_capital += 1

    total_huerfanos += 1

    continuar = input("¿Desea ingresar otro niño? (s/n): ")
    if continuar.lower() != "s":
        break

porcentaje_tachira = (huerfanos_tachira * 100) / total_huerfanos
porcentaje_dc = (huerfanos_distrito_capital * 100) / total_huerfanos
porcentaje_ninos = (huerfanos_ninos * 100) / total_huerfanos
porcentaje_ninas = (huerfanos_ninas * 100) / total_huerfanos


print("RESULTADOS")

print("Porcentaje de huérfanos:")
print("Táchira:", porcentaje_tachira, "%")
print("Distrito Capital:", porcentaje_dc, "%")

print("\nb. Número de huérfanos por grupo de edad:")
print("Grupo 1 (menores de 1 año):", grupo1)
print("Grupo 2 (1 a 3 años):", grupo2)
print("Grupo 3 (4 a 6 años):", grupo3)
print("Grupo 4 (mayores de 6 años):", grupo4)

print("Cantidad y porcentaje por sexo:")
print("Niños:", huerfanos_ninos, "=", porcentaje_ninos, "%")
print("Niñas:", huerfanos_ninas, "=", porcentaje_ninas, "%")