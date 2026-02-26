
p=float(input("Ingrese el valor: "))
q=float(input("Ingrese el valor: "))

operacion= p**3 + q**4 - 2*p**2

if operacion > 680:
   print("Este es el valor de p ", p)
   print("Estes es el valor de q", q)
   print("Este es el valor de la operacion: ", operacion)

else:
    print("La operacion no es mayor que 680")