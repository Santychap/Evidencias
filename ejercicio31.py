
kilometros =float(input("Ingrese los kilometros recorridos: "))

if kilometros > 300:
    print ("El coductor debe pagar 5000 bolivares")

elif kilometros > 300 and kilometros < 1000:
    extra = kilometros - 300
    total = 5000 + (extra * 200)
    print("El conductor debe pagar 200 bolivares", total)

elif kilometros > 1000:
    extra_1000 = kilometros - 1000
    total = 5000 + (700 * 200) + (extra_1000 * 150)
    print("5000 bolivares debe pagar ", total)

    