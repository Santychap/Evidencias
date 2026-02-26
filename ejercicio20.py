

capital = float(input("Ingrese el capital (X): "))
interes = float(input("Ingrese el interés pagado (Y): "))
tiempo = 4

razon = (interes * 100) / (capital * tiempo)

print("El porcentaje anual cobrado es:", razon, "%")