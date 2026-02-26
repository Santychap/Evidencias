sueldo = float(input("Sueldo: "))
ventas = 0

for i in [1, 2, 3]:
    ventas += float(input(f"Venta {i}: "))

if ventas > 0:
    print(f"Comisión: {ventas * 0.1}")
    print(f"Total: {sueldo + (ventas * 0.1)}")
else:
    print("No se realizaron ventas.")