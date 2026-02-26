depar1 = float(input("Ingrese las ventas del departamento 1: "))
depar2 = float(input("Ingrese las ventas del departamento 2: "))
depar3 = float(input("Ingrese las ventas del departamento 3: "))

salario = float(input("Ingrese el salario mensual de los vendedores: "))

total_ventas = depar1 + depar2 + depar3

limite = total_ventas * 0.33


if depar1 > limite:
    total1 = salario + (salario * 0.20)
else:
    total1 = salario


if depar2 > limite:
    total2 = salario + (salario * 0.20)
else:
    total2 = salario


if depar3 > limite:
    total3 = salario + (salario * 0.20)
else:
    total3 = salario

print("Total que reciben los vendedores del departamento 1:", total1)
print("Total que reciben los vendedores del departamento 2:", total2)
print("Total que reciben los vendedores del departamento 3:", total3)