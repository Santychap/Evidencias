

metros = float(input("Metros a convertir: "))


pulgadas_totales = metros * 39.27

pies = int(pulgadas_totales // 12)
pulgadas_restantes = pulgadas_totales % 12

print("Pies:", pies)
print("Pulgadas:", pulgadas_restantes)
