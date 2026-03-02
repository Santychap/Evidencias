


def suma_serie():
    suma = 0
    termino = 1
    contador = 0

    while suma < 1.99:
        suma += termino
        termino = termino / 2
        contador += 1

    print("Número de términos:", contador)
    print("Valor de la suma:", suma)

while True:
    print("\n--- SISTEMA  SUMAS---")
    print("1. Suma")
    print("2. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        suma_serie() 
    elif opcion == "2":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida.")