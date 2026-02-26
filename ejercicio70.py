dias = 0

errores = 0

suma_max = 0

suma_min = 0

temp_max = float(input("Ingrese temperatura máxima: "))
temp_min = float(input("Ingrese temperatura mínima: "))

while temp_max != 0 or temp_min != 0:
    dias += 1
    if temp_max < 14 or temp_max > 30 or temp_min < 14 or temp_min > 30:
        errores += 1
    else:
        suma_max += temp_max
        suma_min += temp_min

    temp_max = float(input("Ingrese temperatura máxima: "))
    temp_min = float(input("Ingrese temperatura mínima: "))
    
if dias > 0:
    media_max = suma_max / dias
    media_min = suma_min / dias
    porcentaje_errores = (errores * 100) / dias
else:
    media_max = 0
    media_min = 0
    porcentaje_errores = 0

print("Número de días:", dias)
print("Media de temperaturas máximas:", media_max)
print("Media de temperaturas mínimas:", media_min)
print("Cantidad de errores:", errores)
print("Porcentaje de errores:", porcentaje_errores, "%")