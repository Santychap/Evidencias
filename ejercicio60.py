opcion = "s"

while opcion == "s":
    num_fac = input("Ingrese el número de la factura: ")
    nom_cli = input("Ingrese el nombre del cliente: ")
    mon_fac = float(input("Ingrese el monto de la factura: "))
    fec_com = int(input("Ingrese el día de compra: "))
    fec_pag = int(input("Ingrese el día de pago: "))

    dias = fec_pag - fec_com

    interes = 0
    descuento = 0

    if dias > 60:
        interes = mon_fac * 0.08

    elif dias >= 31 and dias <= 59:
        interes = mon_fac * 0.06

    elif dias < 15:
        descuento = mon_fac * 0.02

    monto_total = mon_fac + interes - descuento

    print("\n--- FACTURA ---")
    print("Número de factura:", num_fac)
    print("Cliente:", nom_cli)
    print("Monto factura:", mon_fac)
    print("Interés de mora:", interes)
    print("Descuento por pronto pago:", descuento)
    print("Monto total a pagar:", monto_total)

    opcion = input("\n¿Desea ingresar otra factura? (s/n): ")