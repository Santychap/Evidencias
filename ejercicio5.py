
califi1 = float(input("Ingrese la calificacion del parcial 1: "))
califi2 = float(input("Ingrese la calificacion 2: "))
califi3 = float(input("Ingrese la calificacion 3: "))

examen_final = float(input("Ingrese la calificacion del examen final"))
trabajo = float(input("Ingrese la calificacion del trabajo final"))

calificacion_parcial = (califi1 + califi2 + califi3) / 3


calficacion_final = (calificacion_parcial * 0.55) + (examen_final * 0.30) + (trabajo * 0.15)

print("La calificacion final es: ", calficacion_final)