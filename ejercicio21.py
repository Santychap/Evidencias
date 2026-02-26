
x = float(input("Ingrese la cantidad de naranjas (X): "))
y = float(input("Ingrese el precio por docena (Y): "))
k = float(input("Ingrese el monto obtenido por la venta (K): "))

costo_total = (x / 12) * y
ganacia = k - costo_total
porcentaje_ganancia = (ganacia / costo_total) * 100
print("El porcentaje de ganancia obtenida en la inversión es:", porcentaje_ganancia, "%")



