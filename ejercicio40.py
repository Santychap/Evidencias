
lectura_anterior = float(input("Ingrese la lectura anterior (Kwh): "))
lectura_actual = float(input("Ingrese la lectura actual (Kwh): "))
consumo = lectura_actual - lectura_anterior

if consumo < 0:
    print("Error: La lectura actual debe ser mayor a la anterior.")
else:
    if 0 <= consumo <= 100:
        monto_luz = 2622.00
    elif 101 <= consumo <= 300:
        monto_luz = consumo * 79.78
    elif 301 <= consumo <= 500:
        monto_luz = consumo * 89.52
    else: 
        monto_luz = consumo * 97.95

    print("-" * 30)
    print("Consumo total:  Kwh", consumo)
    print("Monto total a pagar:  Bs.", monto_luz)
    print("-" * 30)
