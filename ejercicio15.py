
lectura_anterior = float(input("Ingrese lectura anterior: "))
lectura_actual = float(input("Ingrese lectura actual: "))
costo_kilovatio = float(input("Ingrese costo por kilovatio: "))

consumo = lectura_actual - lectura_anterior
monto_total = consumo * costo_kilovatio

print("Consumo del mes:", consumo, "kWh")
print("Monto total a pagar:", monto_total, "Bs.")
