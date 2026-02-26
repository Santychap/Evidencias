
inversion_total = float(input("Inversion total: "))
monto_hipoteca = float(input("Monto hipoteca: "))

if monto_hipoteca < 1000000:
    pago_persona = inversion_total * 0.5
    pago_socio = inversion_total * 0.5
else:
    resto = inversion_total - monto_hipoteca
    pago_persona = monto_hipoteca + (resto / 2)
    pago_socio = resto / 2

print("Inversion persona:", pago_persona)
print("Inversion socio:", pago_socio)

