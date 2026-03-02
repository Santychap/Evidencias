

def es_perfecto():
    contador_perfectos = 0
    numero = 1

    while contador_perfectos < 3:
        suma = 0
        
        for i in range(1, (numero // 2) + 1):
            if numero % i == 0:
                suma = suma + i
        
        if suma == numero:
            print(numero)
            contador_perfectos = contador_perfectos + 1
        
        numero = numero + 1

        
while True:
    print("SISTEMA  VIAJES")
    print("1. Es perfecto")
    print("2. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        es_perfecto() 
    elif opcion == "2":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida.")