
monto=float(input("Ingrese el monto de la compra"))
if monto < 500:
    print("No hay descuento")

elif monto >=500 and monto <=1000:
  descuento = monto * 0.05
  total = monto - descuento
  print("El total de su compra con el 5% de descueto es: ", total)

elif monto >=1000 and monto < 7000:
  descuento = monto * 0.11
  total = monto - descuento
  print("El total de su compra con el 11% de descueto es: ", total)

elif monto >=7000 and monto < 15000:
  descuento = monto * 0.18
  total = monto - descuento
  print("El total de su compra con el 18% de descueto es: ", total)

elif monto > 15000:
  descuento = monto * 0.25
  total = monto - descuento
  print("El total de su compra con el 25% de descueto es: ", total)

