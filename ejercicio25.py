
salario = float(input("ingrese el salario del trabajador: "))

if salario < 4000:
    aumento = salario * 0.15
    salario_final = salario + aumento
else:
    aumento = salario * 0.12
    salario_final = salario + aumento
    
print("El aumento es:", aumento)
print("El salario final es:", salario_final)