
suma = 0
k = 1
while suma < 1000:
    termino = (k**2 + 1) / k
    if suma + termino > 1000:
        break
    suma += termino
    k += 1
print("El número de términos necesarios para que la sumatoria se aproxime a 1000 sin excederlo es: ", k-1)
