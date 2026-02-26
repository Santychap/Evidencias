
hectareas = float(input("Ingrese el número de hectáreas: "))
m2_totales = hectareas * 10000

if m2_totales > 1000000:
    p_pino, p_oyamel, p_cedro = 0.70, 0.20, 0.10
else:
    p_pino, p_oyamel, p_cedro = 0.50, 0.30, 0.20

m2_pino = m2_totales * p_pino
m2_oyamel = m2_totales * p_oyamel
m2_cedro = m2_totales * p_cedro

cant_pinos = (m2_pino * 8) / 10
cant_oyamel = (m2_oyamel * 15) / 15
cant_cedro = (m2_cedro * 10) / 18

print("\nBosque de", hectareas, "hectáreas (", m2_totales, "m2):")
print("Número de Pinos a sembrar:  ", int(cant_pinos))
print("Número de Oyameles a sembrar:", int(cant_oyamel))
print("Número de Cedros a sembrar:  ", int(cant_cedro))



    
