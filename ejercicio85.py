
extensiones = []
precios = []
N_departamentos = int(input("Ingrese el número de departamentos: "))
for i in range(N_departamentos):
    extension = float(input("Ingrese la extensión del departamento en metros cuadrados: "))
    precio = float(input("Ingrese el precio de alquiler del departamento: "))
    extensiones.append(extension)
    precios.append(precio)
for i in range(N_departamentos):
    for j in range(i + 1, N_departamentos):
        if extensiones[i] > extensiones[j]:
            extensiones[i], extensiones[j] = extensiones[j], extensiones[i]
            precios[i], precios[j] = precios[j], precios[i]
def eliminar_departamento(extension_buscada, precio_buscado):
    for i in range(len(extensiones)):
        if extensiones[i] == extension_buscada and precios[i] == precio_buscado:
            del extensiones[i]
            del precios[i]
            print("Departamento eliminado.")
            return
    print("No se encontró un departamento con la extensión y el precio buscados.")
def actualizar_departamento(extension_vencida):
    for i in range(len(extensiones)):
        if extensiones[i] == extension_vencida:
            del extensiones[i]
            del precios[i]
            print("Departamento actualizado.")
            return
    print("No se encontró un departamento con la extensión vencida.")