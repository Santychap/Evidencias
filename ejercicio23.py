
M = float(input("Ingrese la cantidad de kilogramos de harina: "))
N = float(input("Ingrese la cantidad de litros de aceite obtenidos por tonelada de maíz: "))
B1 = float(input("Ingrese el precio de cada bulto de harina (Bs.): "))
B2 = float(input("Ingrese el precio de cada caja de aceite (Bs.): "))
B3 = float(input("Precio kg harina detal (Bs.): ").replace(",", "."))
B4 = float(input("Precio litro aceite detal (Bs.): ").replace(",", "."))

bultos = M // 24
sobrante_harina = M % 24
ingreso_harina = bultos * B1 + sobrante_harina * B3

cajas = N // 15
sobrante_aceite = N % 15
ingreso_aceite = cajas * B2 + sobrante_aceite * B4

ingreso_total = ingreso_harina + ingreso_aceite

print("Ingreso total por tonelada de maíz:", ingreso_total)