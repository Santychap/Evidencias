
while True:
    estado_codigo = input("Ingrese el código del Estado (o 'salir' para terminar): ")
    if estado_codigo.lower() == 'salir':
        break

    ciudad_codigo = input("Ingrese el código de la Ciudad: ")
    municipio_codigo = input("Ingrese el código del Municipio: ")

    personas = []
    while True:
        edad = int(input("Ingrese la edad de la persona (o -1 para terminar): "))
        if edad == -1:
            break
        nivel_educacion = input("Ingrese el nivel de educación (N, B, S, P): ")
        situacion_actual = input("Ingrese la situación actual (D, E): ")
        personas.append({'edad': edad, 'nivel_educacion': nivel_educacion, 'situacion_actual': situacion_actual})

    
    desempleados_sin_educacion_mayores_25 = sum(1 for persona in personas if persona['situacion_actual'] == 'D' and persona['nivel_educacion'] == 'N' and persona['edad'] > 25)
    print(f"Municipio {municipio_codigo}: Cantidad de personas desempleadas, sin educación y mayores de 25 años: {desempleados_sin_educacion_mayores_25}")

    