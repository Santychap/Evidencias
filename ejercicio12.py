
nota1 = float(input("Ingrese la nota del examen de Matemática: "))
tarea1_mate = float(input("Ingrese la nota de la tarea 1 de Matemática: "))
tarea2_mate = float(input("Ingrese la nota de la tarea 2 de Matemática: "))
tarea3_mate = float(input("Ingrese la nota de la tarea 3 de Matemática: "))
promedio_tareas_mate = (tarea1_mate + tarea2_mate + tarea3_mate) / 3
promedio_final_mate = nota1 * 0.9 + promedio_tareas_mate * 0.1

nota2 = float(input("Ingrese la nota del examen de Fisica"))
tarea1_fis = float(input("Ingrese la nota de l atarea 1 de fisica: "))
tarea2_fis = float(input("Ingrese la nota de la tarea 2 de fisica: "))
promedio_tareas_fis = (tarea1_fis + tarea2_fis) / 2
promedio_final_fis = nota2 * 0.80 + promedio_tareas_fis * 0.2

nota3 = float(input("Ingrese la nota del excamen de Quimica"))
tarea1_qui = float(input("Ingrese la nota de la tarea 1 de quimica: "))
tarea2_qui = float(input("Ingrese la nota de la tarea 2 de quimica: "))
tarea3_qui = float(input("Ingrese la nota de la tarea 3 de quimica: "))

promedio_tareas_qui = (tarea1_qui + tarea2_qui + tarea3_qui ) / 3
promedio_final_qui = nota3 * 0.85 + promedio_tareas_qui * 0.15


print ("Este es le promedio final de matamaticas: ", promedio_final_mate)
print ("Este es le promedio final de Fisica: ", promedio_final_fis)
print ("Este es le promedio final de Quimica: ", promedio_final_qui)
