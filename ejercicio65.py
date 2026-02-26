opcion = "s"

while opcion == "s":
    nombre = input("Nombre del empleado: ")
    cedula = input("Cédula: ")
    tipo = input("Tipo (obrero / administrativo / ejecutivo): ")
    hijos = int(input("Número de hijos: "))
    asistencia = float(input("Porcentaje de asistencia: "))

    if tipo == "obrero":
        sueldo_basico = 100000
    elif tipo == "administrativo":
        sueldo_basico = 165500
    else:
        sueldo_basico = 250000

    # Aportes
    if hijos > 5:
        hijos = 5
    aporte_hijos = sueldo_basico * 0.10 * hijos

    if asistencia > 95:
        aporte_asistencia = sueldo_basico * 0.05
    else:
        aporte_asistencia = 0

    # Deducciones
    caja_ahorro = sueldo_basico * 0.10
    seguro_social = sueldo_basico * 0.02

    sueldo_neto = sueldo_basico + aporte_hijos + aporte_asistencia - caja_ahorro - seguro_social

    print("\nEmpleado:", nombre)
    print("Cédula:", cedula)
    print("Sueldo básico:", sueldo_basico)
    print("Caja de ahorros:", caja_ahorro)
    print("Seguro social:", seguro_social)
    print("Sueldo neto:", sueldo_neto)

    opcion = input("\n¿Desea ingresar otro empleado? (s/n): ")