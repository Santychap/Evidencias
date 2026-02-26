total_empresas = 0

agricolas = 0
mineras_sur = 0

cont_agricola = 0
cont_industrial = 0
cont_minera = 0
cont_pesquera = 0
cont_otra = 0

opcion = "s"
while opcion == "s":
    actividad = input("Actividad: ")
    localizacion = input("Localización: ")
    número_trabajadores = int(input("Número de trabajadores: "))
    total_empresas += 1

    if actividad == 1:
        cont_agricola += 1
        agricolas += 1
    elif actividad == 2:
        cont_industrial += 1
    elif actividad == 3:
        cont_minera += 1
        if localizacion == 2:
            mineras_sur += 1
    elif actividad == 4:
        cont_pesquera += 1
    elif actividad == 5:
        cont_otra += 1

    opcion = input("¿Desea ingresar otra empresa? (s/n): ")


porc_agricolas = (agricolas / total_empresas) * 100
porc_mineras_sur = (mineras_sur / cont_minera) * 100


mayor = cont_agricola
tipo = "Agrícola"

if cont_industrial > mayor:
    mayor = cont_industrial
    tipo = "Industrial"
if cont_minera > mayor:
    mayor = cont_minera
    tipo = "Minera"
if cont_pesquera > mayor:
    mayor = cont_pesquera
    tipo = "Pesquera"
if cont_otra > mayor:
    mayor = cont_otra
    tipo = "Otra"

print("Porcentaje de empresas agrícolas:", porc_agricolas)
print("Porcentaje de mineras del sur:", porc_mineras_sur)
print("Actividad con más empresas:", tipo)