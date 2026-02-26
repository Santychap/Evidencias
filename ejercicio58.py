capital = float(input("Ingrese el capital a depositar: "))
tasa = float(input("Ingrese la tasa de interés (ejemplo 0.06): "))
semanas = float(input("Ingrese la duración en semanas: "))

dias = semanas * 7
contador = 0

while contador < dias:
    interes_diario = (tasa * capital) / 365
    capital = capital + interes_diario
    contador = contador + 1

print("El capital total acumulado es:", capital)