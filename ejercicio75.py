persona = 1

while persona <= 5:
    print("\nPersona", persona)
    peso_anterior = float(input("Peso anterior: "))

    suma = 0
    i = 0
    while i < 10:
        peso = float(input("Peso en báscula: "))
        suma += peso
        i += 1

    promedio = suma / 10
    diferencia = promedio - peso_anterior

    if diferencia > 0:
        print("SUBIÓ", diferencia, "kg")
    else:
        print("BAJÓ", abs(diferencia), "kg")

    persona += 1