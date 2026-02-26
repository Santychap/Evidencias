def decidir_compra():

    precio_inicial = float(input("Ingrese el costo del automóvil y terreno: "))
    devaluacion_porcentaje = float(input("Ingrese el % de devaluación anual del auto: "))
    apreciacion_porcentaje = float(input("Ingrese el % de aumento de valor anual del terreno: "))

    devaluacion_total = precio_inicial * (devaluacion_porcentaje / 100) * 3
    
    incremento_terreno = precio_inicial * (apreciacion_porcentaje / 100) * 3
   
    if devaluacion_total <= (incremento_terreno / 2):
        print("Resultado: Comprar el automóvil.")
    else:
        print("Resultado: No comprar el automóvil (mejor comprar terreno).")

decidir_compra()
