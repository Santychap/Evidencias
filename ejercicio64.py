suma = 0
termino = 1
contador = 0

while suma < 1.99:
    suma += termino
    termino = termino / 2
    contador += 1

print("Número de términos:", contador)
print("Valor de la suma:", suma)