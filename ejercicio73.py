
fecha_consulta = input("Ingrese la fecha de consulta (dd/mm/aaaa): ")

suma_mayores_agencias = 0
contador_agencias = 0


while True:
    codigo_estado = input("Código del estado: ")

    total_estado = 0
    mayor_monto_agencia = 0
    menor_monto_agencia = 999999999
    codigo_agencia_mayor = ""
    codigo_agencia_menor = ""


    while True:
        codigo_agencia = input("Código de la agencia: ")

        total_agencia = 0
        clientes_con_deuda = 0
        mayor_deuda_cliente = 0
        codigo_cliente_mayor = ""

        
        while True:
            codigo_cliente = input("Código del cliente: ")
            nombre = input("Nombre: ")
            direccion = input("Dirección: ")

            print("RECIBO DEL CLIENTE")
            print("Cliente:", codigo_cliente, nombre, direccion)
            print("Estado:", codigo_estado, "Agencia:", codigo_agencia)

            total_cliente = 0
            contador_pagares = 0

        
            while True:
                num_pagare = input("Número de pagaré: ")
                fecha_venc = input("Fecha de vencimiento: ")
                monto = float(input("Monto del pagaré: "))

                if fecha_venc <= fecha_consulta:
                    print(num_pagare, fecha_venc, monto)
                    total_cliente += monto
                    contador_pagares += 1

                op_pagare = input("¿Otro pagaré? (s/n): ")

            if contador_pagares > 0:
                print("Cantidad de pagarés:", contador_pagares)
                print("Total pendiente:", total_cliente)

                clientes_con_deuda += 1
                total_agencia += total_cliente

                if total_cliente > mayor_deuda_cliente:
                    mayor_deuda_cliente = total_cliente
                    codigo_cliente_mayor = codigo_cliente

            op_cliente = input("¿Otro cliente? (s/n): ")

        print("AGENCIA:", codigo_agencia)
        print("Clientes con deuda:", clientes_con_deuda)
        print("Monto total adeudado:", total_agencia)
        print("Cliente con mayor deuda:", codigo_cliente_mayor)

        total_estado += total_agencia

        if total_agencia > mayor_monto_agencia:
            mayor_monto_agencia = total_agencia
            codigo_agencia_mayor = codigo_agencia

        if total_agencia < menor_monto_agencia:
            menor_monto_agencia = total_agencia
            codigo_agencia_menor = codigo_agencia

        suma_mayores_agencias += mayor_monto_agencia
        contador_agencias += 1

        op_agencia = input("¿Otra agencia? (s/n): ")

    print("ESTADO:", codigo_estado)
    print("Monto total adeudado:", total_estado)
    print("Agencia con mayor monto:", codigo_agencia_mayor)
    print("Agencia con menor monto:", codigo_agencia_menor)

    op_estado = input("¿Otro estado? (s/n): ")

if contador_agencias > 0:
    promedio = suma_mayores_agencias / contador_agencias
    print("Promedio nacional de montos máximos por agencia:", promedio)