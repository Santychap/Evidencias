edad_meses = float(input("Ingrese la edad en MESES (si tiene años, multiplique por 12): "))
hemoglobina = float(input("Ingrese el nivel de hemoglobina (g%): "))
nivel_minimo = 0

if 0 <= edad_meses <= 1:
    nivel_minimo = 13
elif 1 < edad_meses <= 6:
    nivel_minimo = 10
elif 6 < edad_meses <= 12:
    nivel_minimo = 11
elif 12 < edad_meses <= 60: 
    nivel_minimo = 11.5
elif 60 < edad_meses <= 120: 
    nivel_minimo = 12.6
elif 120 < edad_meses <= 180: 
    nivel_minimo = 13
else:
    sexo = input("Ingrese el sexo (H para hombre, M para mujer): ").upper()
    if sexo == "M":
        nivel_minimo = 12
    else:
        nivel_minimo = 14

if hemoglobina < nivel_minimo:
    resultado = "POSITIVO (Tiene Anemia)"
else:
    resultado = "NEGATIVO (No tiene Anemia)"

print("Resultado del análisis: ", resultado)
print("El nivel mínimo para su edad/sexo es:", nivel_minimo, "g%")
