intereses = float(input("Ingrese el monto de intereses generados: "))
capital = float(input("Ingrese el monto de capital invertido: "))

print("El dinero generado por concepto de intereses es:", intereses)

if intereses > 7000:
    capital_final = capital + intereses
    print("Los intereses se reinvierten.")
    print("El dinero final en la cuenta es:", capital_final)
else:
    print("Los intereses no se reinvierten.")
    print("El dinero final en la cuenta es:", capital)