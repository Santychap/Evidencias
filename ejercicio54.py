def cuestionarios():
    total_puntos = 0
    total_cuestionarios = 64
    promedios = []

    for i in range(total_cuestionarios):
        puntos_cuestionario = 0
        print(f"\n--- Llenando Instrumento #{i+1} ---")
        
        for j in range(23):
            while True:
                respuesta = int(input(f"Pregunta {j+1} (1-5): "))
                if 1 <= respuesta <= 5:
                    puntos_cuestionario += respuesta
                    break
                else:
                    print("¡Error! La respuesta debe estar entre 1 y 5.")
        
        promedio_cuestionario = puntos_cuestionario / 23
        promedios.append(promedio_cuestionario)
        total_puntos += puntos_cuestionario


    promedio_general = total_puntos / (total_cuestionarios * 23)
    promedio_mas_alto = max(promedios)
    promedio_mas_bajo = min(promedios)
    
   
    instrumento_mas_alto = promedios.index(promedio_mas_alto) + 1
    instrumento_mas_bajo = promedios.index(promedio_mas_bajo) + 1
    
    
    inf_3 = sum(1 for p in promedios if p < 3)
    sup_4 = sum(1 for p in promedios if p > 4)
    entre_45_5 = sum(1 for p in promedios if 4.5 <= p <= 5)
    
    porc_inf_3_vs_sup_4 = (inf_3 / sup_4) * 100 if sup_4 > 0 else 0
    porc_total_45_5 = (entre_45_5 / total_cuestionarios) * 100

    print("\n" + "="*50)
    print(f"a. Promedio general: {promedio_general:.2f}")
    print(f"b. Mayor promedio: {promedio_mas_alto:.2f} (Instrumento {instrumento_mas_alto})")
    print(f"c. Menor promedio: {promedio_mas_bajo:.2f} (Instrumento {instrumento_mas_bajo})")
    print(f"d. Porcentaje < 3 respecto a > 4: {porc_inf_3_vs_sup_4:.2f}%")
    print(f"e. Porcentaje [4.5 - 5] del total: {porc_total_45_5:.2f}%")
    print("="*50)

while True:
    print("SISTEMA DE INVESTIGACIÓN")
    print("1. Iniciar carga de datos")
    print("2. Salir")
    
    opcion = input("Elige una opción: ")

    if opcion == "1":
        cuestionarios() 
    elif opcion == "2":
        print("Saliendo... ¡Éxito en tu investigación!")
        break
    else:
        print("Opción no válida.")
