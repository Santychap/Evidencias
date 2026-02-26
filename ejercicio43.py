
capital = float(input("Ingrese su capital actual: "))

if capital < 0:
    nuevo_saldo = 10000
    prestamo = nuevo_saldo - capital
elif capital <= 20000:
    nuevo_saldo = 20000
    prestamo = nuevo_saldo - capital
else:
    nuevo_saldo = capital
    prestamo = 0

resto = nuevo_saldo - 7000
insumos = resto / 2
incentivos = resto / 2

print("Prestamo del banco:", prestamo)
print("Dinero para insumos:", insumos)
print("Dinero para incentivos:", incentivos)

