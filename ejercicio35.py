
temp = float(input("Ingrese la temperatura: "))

if temp > 85:
    print("Natación")

elif 70 < temp < 85:
    print("Tenis")

elif 32 < temp < 70:
    print("Golf")

elif 10 < temp < 32:
    print("Esquí")

elif temp <= 10:
    print("Marcha")
