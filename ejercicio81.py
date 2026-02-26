
while True:
    est_nom = input("Nombre del Estado (o 'fin' para salir): ")
    if est_nom.lower() == 'fin': break
    est_cod = input("Código del Estado (2 dígitos): ")

    total_neto_estado = 0
    ciudades_bajo_esperado = 0
    ciudades_exito_40_60 = 0
    total_ciudades = 0

    cant_ciudades = int(input(f"¿Cuántas ciudades procesará en {est_nom}?: "))
    
    for _ in range(cant_ciudades):
        ciu_nom = input("Nombre de la Ciudad: ")
        ciu_cod = input("Código de Ciudad (3 dígitos, termina en el cod. estado): ")
        unidades_esperadas = int(input("Unidades de venta esperadas: "))
        
    
        total_unidades_ciu = 0
        monto_bruto_ciu = 0
        comision_tienda_ciu = 0
        comision_calle_ciu = 0
        mejor_canal_cod = ""
        max_monto_neto_canal = -1
        vendedor_min_unidades_cod = ""
        min_unidades_vendedor = float('inf')

        cant_canales = int(input(f"¿Cuántos canales tiene {ciu_nom}?: "))
        for _ in range(cant_canales):
            can_cod = input("Código de Canal (4 dígitos): ")
            monto_neto_canal = 0

            cant_vendedores = int(input(f"¿Cuántos vendedores en canal {can_cod}?: "))
            for _ in range(cant_vendedores):
                vend_cod = input("Código Vendedor (5 dígitos): ")
                unidades = int(input("Unidades vendidas: "))
                monto = float(input("Monto total vendido ($): "))

                tipo = vend_cod[:2] 
                comision = 0
                if tipo == "11": 
                    comision = monto * 0.10
                    comision_tienda_ciu += comision
                elif tipo == "12": 
                    comision = monto * 0.15
                    comision_calle_ciu += comision
                
       
                total_unidades_ciu += unidades
                monto_bruto_ciu += monto
                monto_neto_canal += (monto - comision)

                if unidades < min_unidades_vendedor:
                    min_unidades_vendedor = unidades
                    vendedor_min_unidades_cod = vend_cod

            if monto_neto_canal > max_monto_neto_canal:
                max_monto_neto_canal = monto_neto_canal
                mejor_canal_cod = can_cod

  
        print(f"\n--- REPORTE CIUDAD: {ciu_nom} ---")
        print(f"Código: {ciu_cod} | Unidades: {total_unidades_ciu} | Bruto: ${monto_bruto_ciu}")
        print(f"Comisión Tienda: ${comision_tienda_ciu} | Calle: ${comision_calle_ciu}")
        print(f"Mejor Canal: {mejor_canal_cod} | Vendedor menos ventas: {vendedor_min_unidades_cod}")

        total_ciudades += 1
        monto_neto_ciudad = monto_bruto_ciu - (comision_tienda_ciu + comision_calle_ciu)
        total_neto_estado += monto_neto_ciudad

        if total_unidades_ciu < unidades_esperadas:
            ciudades_bajo_esperado += 1
        
 
        if (unidades_esperadas * 1.4) <= total_unidades_ciu <= (unidades_esperadas * 1.6):
            ciudades_exito_40_60 += 1


    porc_no_alcanzaron = (ciudades_bajo_esperado / total_ciudades) * 100 if total_ciudades > 0 else 0
    print(f"\ REPORTE ESTADO: {est_nom} ({est_cod}) ")
    print(f"Monto Neto Total: ${total_neto_estado}")
    print(f"Ciudades que no alcanzaron la meta: {porc_no_alcanzaron}%")
    print(f"Ciudades con 40%-60% sobre meta: {ciudades_exito_40_60}")
  
