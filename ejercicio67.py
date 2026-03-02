
deuda = 12775
pago = 100
incremento = 125
contador = 0

print("Pago\tDeuda pendiente")

while deuda > 0:

    if contador == 0:   
        monto = pago
    else:          
        monto = pago

    if monto > deuda:   
        monto = deuda

    deuda = deuda - monto
    contador = contador + 1

    print(monto, "\t", deuda)

    pago = pago + incremento  

print("Número de pagos:", contador)
print("Monto del último pago:", monto)