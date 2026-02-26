
pvp1 = 100
pvp2 = 200
pvp3 = 300

contador_sucursales = 0
sucursales_cumplen = 0


while True:
    codigo_sucursal = input("\nCódigo de la sucursal: ")
    descripcion = input("Descripción: ")
    venta_esperada = float(input("Monto esperado de venta: "))

    total_sucursal = 0
    mayor_comision_punto = 0
    codigo_punto_mayor = ""

    
    while True:
        codigo_punto = input("\nCódigo del punto de venta: ")

        u1 = int(input("Unidades producto 1: "))
        u2 = int(input("Unidades producto 2: "))
        u3 = int(input("Unidades producto 3: "))

        unidades_totales = u1 + u2 + u3
        venta_bruta = u1*pvp1 + u2*pvp2 + u3*pvp3

        comision = venta_bruta * 0.10
        venta_neta = venta_bruta - comision

        menor = u1
        prod_menor = 1

        if u2 < menor:
            menor = u2
            prod_menor = 2
        if u3 < menor:
            menor = u3
            prod_menor = 3

        print("\nPUNTO DE VENTA:", codigo_punto)
        print("Unidades vendidas:", unidades_totales)
        print("Monto neto:", venta_neta)
        print("Comisión:", comision)
        print("Producto con menor venta:", prod_menor)

        total_sucursal += venta_neta

        if comision > mayor_comision_punto:
            mayor_comision_punto = comision
            codigo_punto_mayor = codigo_punto

        op_punto = input("\n¿Otro punto de venta? (s/n): ")

    porcentaje = (total_sucursal / venta_esperada) * 100

    print("\nSUCURSAL:", codigo_sucursal)
    print("Descripción:", descripcion)
    print("Total vendido:", total_sucursal)
    print("Porcentaje alcanzado:", porcentaje, "%")
    print("Punto con mayor comisión:", codigo_punto_mayor, "-", mayor_comision_punto)

    if total_sucursal >= venta_esperada:
        sucursales_cumplen += 1

    contador_sucursales += 1
    op_sucursal = input("¿Otra sucursal? (s/n): ")

porcentaje_sucursales = (sucursales_cumplen / contador_sucursales) * 100
print("Porcentaje de sucursales que cumplieron la meta:", porcentaje_sucursales, "%")