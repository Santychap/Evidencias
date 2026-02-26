sueldo = float(input("Ingrese el sueldo del trabajador: "))
categoria = float(input("Ingrese la categoria 1, 2, 3 o 4"))
if categoria == 1:
    aumento = sueldo * 0.15
    total = sueldo + aumento
    print("La categoria es: ", categoria)
    print("Su nuevo sueldo es: ", total)

elif categoria == 2:
    aumento = sueldo * 0.10
    total = sueldo + aumento
    print("La categoria es: ", categoria)
    print("Su nuevo sueldo es: ", total)

elif categoria == 3:
    aumento = sueldo * 0.08
    total = sueldo + aumento
    print("La categoria es: ", categoria)
    print("Su nuevo sueldo es: ", total)

elif categoria == 4:
    aumento = sueldo * 0.07
    total = sueldo + aumento
    print("La categoria es: ", categoria)
    print("Su nuevo sueldo es: ", total)