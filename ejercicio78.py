def ventas():
    pvp1, pvp2, pvp3 = 100, 200, 300
    contador_sucursales = 0
    sucursales_cumplen = 0

    while True:
        print(" DATOS DE LA SUCURSAL")
        codigo_sucursal = input("Código de la sucursal: ")
        descripcion = input("Descripción: ")
        venta_esperada = float(input("Monto esperado de venta: "))

        total_sucursal = 0
        mayor_comision = -1
        punto_mayor = ""

        while True:
            print("PUNTO DE VENTA")
            cod_punto = input("Código del punto: ")
            u1 = int(input("Unidades producto 1: "))
            u2 = int(input("Unidades producto 2: "))
            u3 = int(input("Unidades producto 3: "))

            venta_bruta = (u1 * pvp1) + (u2 * pvp2) + (u3 * pvp3)
            comision = venta_bruta * 0.10
            venta_neta = venta_bruta - comision
            total_sucursal = total_sucursal + venta_neta

            menor = u1
            prod_menor = 1
            if u2 < menor:
                menor = u2
                prod_menor = 2
            if u3 < menor:
                menor = u3
                prod_menor = 3

            if comision > mayor_comision:
                mayor_comision = comision
                punto_mayor = cod_punto

            print("Punto de venta:", cod_punto)
            print("Monto neto:", venta_neta)
            print("Comisión:", comision)
            print("Producto con menor venta:", prod_menor)

            op_punto = input("\n¿Otro punto de venta en esta sucursal? (s/n): ")
            if op_punto.lower() == "n":
                break

        porcentaje = (total_sucursal / venta_esperada) * 100
        contador_sucursales = contador_sucursales + 1
        if total_sucursal >= venta_esperada:
            sucursales_cumplen = sucursales_cumplen + 1

        print("\nSUCURSAL:", codigo_sucursal)
        print("Total vendido neto:", total_sucursal)
        print("Porcentaje alcanzado:", porcentaje, "%")
        print("Punto con mayor comisión:", punto_mayor, "con", mayor_comision)

        op_sucursal = input("\n¿Registrar otra sucursal? (s/n): ")
        if op_sucursal.lower() == "n":
            break

 
    if contador_sucursales > 0:
        promedio_cumplimiento = (sucursales_cumplen / contador_sucursales) * 100
        print("REPORTE FINAL")
        print("Porcentaje de sucursales que cumplieron la meta:", promedio_cumplimiento, "%")


while True:
    print("\n--- MENÚ DE OPERACIONES ---")
    print("1. Iniciar registro de ventas")
    print("2. Salir")
    
    opcion = input("Elija una opción: ")

    if opcion == "1":
        ventas()
    elif opcion == "2":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida.")