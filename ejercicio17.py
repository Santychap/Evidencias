
producto = float(input("Ingrese el precio final pagado por el producto: "))
pvp = float(input("Ingrese el precio de venta al público (PVP) del producto: "))

descuento = ((pvp - producto) / pvp) * 100

print("Este es el descuento: ", descuento)