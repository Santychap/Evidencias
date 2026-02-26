contador_perfectos = 0
numero = 1

while contador_perfectos < 3:
    suma = 0
    
    for i in range(1, numero):
        if numero % i == 0:
            suma = suma + i
    
    if suma == numero:
        print(numero)
        contador_perfectos = contador_perfectos + 1
    
    numero = numero + 1