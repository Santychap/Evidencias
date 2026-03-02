def main():
    total_empresas = 0
    cont_agricola = 0
    cont_industrial = 0
    cont_minera = 0
    mineras_sur = 0
    cont_pesquera = 0
    cont_otra = 0

    while True:
        print("Registro de Empresa")
        print("1. Agrícola, 2. Industrial, 3. Minera, 4. Pesquera, 5. Otra")
        actividad = int(input("Seleccione Actividad (1-5): "))
        print("1. Norte, 2. Sur, 3. Centro")
        localizacion = int(input("Seleccione Localización (1-3): "))
        
        total_empresas = total_empresas + 1

        if actividad == 1:
            cont_agricola = cont_agricola + 1
        elif actividad == 2:
            cont_industrial = cont_industrial + 1
        elif actividad == 3:
            cont_minera = cont_minera + 1
            if localizacion == 2:
                mineras_sur = mineras_sur + 1
        elif actividad == 4:
            cont_pesquera = cont_pesquera + 1
        elif actividad == 5:
            cont_otra = cont_otra + 1

        continuar = input("\n¿Desea ingresar otra empresa? (s/n): ")
        if continuar == "n" or continuar == "N":
            break 


    porc_agricolas = (cont_agricola / total_empresas) * 100
    
    
    if cont_minera > 0:
        porc_mineras_sur = (mineras_sur / cont_minera) * 100
    else:
        porc_mineras_sur = 0

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

    print("RESULTADOS FINALES")
    print("Porcentaje de empresas agrícolas:", porc_agricolas, "%")
    print("Porcentaje de mineras del sur:", porc_mineras_sur, "%")
    print("Actividad con más empresas:", tipo)


while True:
    print("SISTEMA DE EMPRESAS")
    print("1. Ingresar empresas")
    print("2. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        main() 
    elif opcion == "2":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida.")
