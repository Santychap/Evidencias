
monto = int(input("Ingrese la cantidad en Bolívares: "))

billetes = [50000, 20000, 10000, 5000, 2000, 1000, 500, 100, 50, 20, 10]

print("Desglose para Bolívares:", monto)

for billete in billetes:
    if monto >= billete:
        cantidad_billetes = monto // billete  
        monto = monto % billete             
        print(f"{cantidad_billetes} billete(s) de {billete}")

if monto > 0:
    print("Sobrante en monedas: ", monto)