
total_puntos = 0
total_cuestionarios = 64
promedios = []
for i in range(total_cuestionarios):
    puntos_cuestionario = 0
    for j in range(23):
        respuesta = int(input(f"Ingrese la respuesta para la pregunta {j+1} del cuestionario {i+1} (1-5): "))
        puntos_cuestionario += respuesta
    promedio_cuestionario = puntos_cuestionario / 23
    promedios.append(promedio_cuestionario)
    total_puntos += puntos_cuestionario
promedio_general = total_puntos / (total_cuestionarios * 23)
promedio_mas_alto = max(promedios)
promedio_mas_bajo = min(promedios)
instrumento_mas_alto = promedios.index(promedio_mas_alto) +1
instrumento_mas_bajo = promedios.index(promedio_mas_bajo) +1
cuestionarios_inferiores_a_3 = sum(1 for p in promedios if p < 3)
cuestionarios_superiores_a_4 = sum(1 for p in promedios if p > 4)
cuestionarios_entre_4_5_y_5 = sum(1 for p in promedios if 4.5 <= p <= 5)
porcentaje_inferiores_a_3 = (cuestionarios_inferiores_a_3 / cuestionarios_superiores_a_4) * 100 if cuestionarios_superiores_a_4 > 0 else 0
porcentaje_entre_4_5_y_5 = (cuestionarios_entre_4_5_y_5 / total_cuestionarios) * 100
print("Promedio general de todos los cuestionarios: ", promedio_general)
print("Promedio más alto obtenido: ", promedio_mas_alto, "corresponde al instrumento: ", instrumento_mas_alto)
print("Promedio más bajo obtenido: ", promedio_mas_bajo, "corresponde al instrumento: ", instrumento_mas_bajo)
print("Porcentaje de cuestionarios con promedio inferior a 3 respecto a los superiores a 4: ", porcentaje_inferiores_a_3, "%")
print("Porcentaje de cuestionarios con promedio entre 4.5 y 5 respecto al total procesado: ", porcentaje_entre_4_5_y_5, "%")    