total_pasajeros = 0
pasajeros_no_pagan = 0

opcion_vuelo = "s"

while opcion_vuelo == "s":
    numero_vuelo = input("Número de vuelo: ")

    total_dinero_vuelo = 0
    mayor_peso_vuelo = 0
    menor_peso_vuelo = 0
    nombre_mayor = ""
    nombre_menor = ""

    opcion_pasajero = "s"

    while opcion_pasajero == "s":
        codigo_abordo = input("Código de abordo: ")
        nombre = input("Nombre del pasajero: ")

        suma_kilos = 0
        mayor_maleta = 0
        codigo_maleta_mayor = ""

        opcion_maleta = "s"

        while opcion_maleta == "s":
            codigo_maleta = input("Código de la maleta: ")
            peso = float(input("Peso de la maleta: "))

            suma_kilos += peso

            if peso > mayor_maleta:
                mayor_maleta = peso
                codigo_maleta_mayor = codigo_maleta

            opcion_maleta = input("¿Otra maleta? (s/n): ")

        if suma_kilos <= 3:
            monto_pagar = 0
        elif suma_kilos <= 6:
            monto_pagar = 600
        elif suma_kilos <= 9:
            monto_pagar = 1200
        elif suma_kilos <= 12:
            monto_pagar = 1500
        elif suma_kilos <= 15:
            monto_pagar = 2000
        else:
            monto_pagar = 2500

        print("Vuelo:", numero_vuelo)
        print("Código:", codigo_abordo)
        print("Nombre:", nombre)
        print("Total kilos:", suma_kilos)
        print("Monto a pagar:", monto_pagar)

        print("Maleta con mayor peso:", codigo_maleta_mayor)

        if suma_kilos > mayor_peso_vuelo:
            mayor_peso_vuelo = suma_kilos
            nombre_mayor = nombre

        if menor_peso_vuelo == 0 or suma_kilos < menor_peso_vuelo:
            menor_peso_vuelo = suma_kilos
            nombre_menor = nombre

        total_dinero_vuelo += monto_pagar
        total_pasajeros += 1

        if monto_pagar == 0:
            pasajeros_no_pagan += 1

        opcion_pasajero = input("¿Otro pasajero? (s/n): ")

    print("Vuelo:", numero_vuelo)
    print("Pasajero con mayor peso:", nombre_mayor)
    print("Pasajero con menor peso:", nombre_menor)
    print("Total dinero del vuelo:", total_dinero_vuelo)

    opcion_vuelo = input("¿Otro vuelo? (s/n): ")

if total_pasajeros > 0:
    porcentaje = (pasajeros_no_pagan * 100) / total_pasajeros
    print("Porcentaje de pasajeros que no pagaron:", porcentaje, "%")