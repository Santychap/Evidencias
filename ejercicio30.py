A = 6
B = 5
C = 2
D = 7

N = A*1000 + B*100 + C*10 + D

ultimos_dos = C*10 + D

if ultimos_dos < 50:
    resultado = (N // 100) * 100
else:
    resultado = ((N // 100) + 1) * 100

print("Número original:", N)
print("Número redondeado a la centena más próxima:", resultado)

