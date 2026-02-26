monto_total = float(input("Ingrese el monto total de la compra: "))

if monto_total > 500000:
    inversion = monto_total * 0.55
    prestamo = monto_total * 0.30
    credito = monto_total * 0.15
else:
    inversion = monto_total * 0.70
    prestamo = 0
    credito = monto_total * 0.30

intereses = credito * 0.20
total_credito = credito + intereses

print("Cantidad a invertir de fondos propios:", inversion)
print("Cantidad pagada a crédito:", credito)
print("Monto a pagar por intereses:", intereses)
print("Total a pagar al fabricante:", total_credito)
print("Cantidad prestada al banco:", prestamo)