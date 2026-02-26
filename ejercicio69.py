A = int(input("Ingrese el primer número (A): "))
B = int(input("Ingrese el segundo número (B): "))

sumaA = 0
sumaB = 0

i = 1
while i < A:
    if A % i == 0:
        sumaA += i
    i += 1

j = 1
while j < B:
    if B % j == 0:
        sumaB += j
    j += 1

print("Suma de divisores de", A, "=", sumaA)
print("Suma de divisores de", B, "=", sumaB)

if sumaA == B and sumaB == A:
    print("Los números son AMIGOS")
else:
    print("Los números NO son amigos")

