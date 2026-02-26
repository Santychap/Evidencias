
p = float(input("Ingrese el precio al contado del computador: "))
t = float(input("Ingrese las T bolivares: "))
total_cuotas = 12 * t
recargo = total_cuotas - p
porcentaje_recargo = (recargo / p) * 100
print("El porcentaje de recargo por pagar en cuotas es: ", porcentaje_recargo)