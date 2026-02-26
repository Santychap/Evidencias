
fecha = input("Ingresa tu fecha (dia/mes): ")
datos = fecha.split("/")
dia = int(datos[0])
mes = int(datos[1])

if (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
    print("Sagitario")
elif (mes == 12 and dia >= 22) or (mes == 1 and dia <= 20):
    print("Capricornio")
elif (mes == 1 and dia >= 21) or (mes == 2 and dia <= 19):
    print("Acuario")
elif (mes == 2 and dia >= 20) or (mes == 3 and dia <= 19):
    print("Piscis")
elif (mes == 3 and dia >= 21) or (mes == 4 and dia <= 20):
    print("Aries")
elif (mes == 4 and dia >= 21) or (mes == 5 and dia <= 21):
    print("Tauro")
elif (mes == 5 and dia >= 22) or (mes == 6 and dia <= 21):
    print("Géminis")
elif (mes == 6 and dia >= 22) or (mes == 7 and dia <= 22):
    print("Cáncer")
elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 23):
    print("Leo")
elif (mes == 8 and dia >= 24) or (mes == 9 and dia <= 22):
    print("Virgo")
elif (mes == 9 and dia >= 24) or (mes == 10 and dia <= 22):
    print("Libra")
elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
    print("Escorpión")
