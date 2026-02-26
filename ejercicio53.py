

nombre = input("Ingrese su nombre: ")
nacionalidad= input ("V o E:")
edad = float(input("Ingrese su edad: "))
tipo_empleado= input("Ingrese su tipo de empleado (1, 2 o 3C): ")
horas_trabajadas = float(input("Ingrese las horas trabajadas: "))


sueldo_base = 0

if tipo_empleado == "1":
    sueldo_base = horas_trabajadas * 5000
elif tipo_empleado == "2":
    sueldo_base = horas_trabajadas * 10000
elif tipo_empleado == "3":
    sueldo_base = horas_trabajadas * 15000
else:
    print("Tipo de empleado no válido.")
    exit()

seguro_social = 0
if sueldo_base > 100000:
    seguro_social = sueldo_base * 0.03
total_venezolanos = 0
if nacionalidad == "V":
    total_venezolanos += sueldo_base
total_extranjeros_impares = 0
if nacionalidad == "E" and int(edad) % 2 != 0:
    total_extranjeros_impares += sueldo_base
total_general = sueldo_base + seguro_social
print("Sueldo básico o bruto: ", sueldo_base)
print("Seguro Social: ", seguro_social)
print("Total de venezolanos por tipo de empleado: ", total_venezolanos)
print("Total de extranjeros cuya edad es impar: ", total_extranjeros_impares)
print("Total general a pagar en sueldos: ", total_general)



