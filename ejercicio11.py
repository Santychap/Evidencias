
nombre = input("Nombre del trabajador: ")
horas_normales = float(input("Horas normales trabajadas: "))
pago_hora_normal = float(input("Pago por hora normal: "))
horas_extras = float(input("Horas extras trabajadas: "))
num_hijos = int(input("Número de hijos: "))

sueldo_base = horas_normales * pago_hora_normal
pago_hora_extra = pago_hora_normal * 1.25
monto_extras = horas_extras * pago_hora_extra

paro_forzoso = sueldo_base * 0.05
politica_habitacional = sueldo_base * 0.02
caja_ahorro = sueldo_base * 0.07
total_deducciones = paro_forzoso + politica_habitacional + caja_ahorro

monto_hijos = num_hijos * 17300
total_asignaciones = 25000 + monto_hijos + 18000

sueldo_neto = (sueldo_base + monto_extras + total_asignaciones) - total_deducciones

print("Trabajador:", nombre)
print("Asignaciones totales:", total_asignaciones, "Bs.")
print("Deducciones totales:", total_deducciones, "Bs.")
print("Sueldo Neto a pagar:", sueldo_neto, "Bs.")
