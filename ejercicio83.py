def resolver_turismo():
   
    CT = ["Playa Azul", "Montaña Verde", "Sol y Arena"]
    TR = [5, 8, 3] 
    H = [20, 30, 40, 15, 25, 25] 
    
    N = len(CT)


    max_restaurantes = -1
    centro_mas_rest = ""
    for i in range(N):
        if TR[i] > max_restaurantes:
            max_restaurantes = TR[i]
            centro_mas_rest = CT[i]
    print(f"a) Centro con más restaurantes: {centro_mas_rest}")

 
    max_sencillas = max_dobles = max_total = -1
    nom_sencillas = nom_dobles = nom_total = ""

    for i in range(N):
        sencillas = H[2*i]
        dobles = H[2*i + 1]
        total = sencillas + dobles
        
        if sencillas > max_sencillas:
            max_sencillas, nom_sencillas = sencillas, CT[i]
        if dobles > max_dobles:
            max_dobles, nom_dobles = dobles, CT[i]
        if total > max_total:
            max_total, nom_total = total, CT[i]

    print(f"b) Más sencillas: {nom_sencillas}, Más dobles: {nom_dobles}, Más total: {nom_total}")

  
    busqueda = input("Ingrese el nombre del centro a consultar: ")
    encontrado = False
    for i in range(N):
        if CT[i].lower() == busqueda.lower():
            total = H[2*i] + H[2*i + 1]
            print(f"c) El centro {CT[i]} tiene {total} habitaciones en total.")
            encontrado = True
            break
    if not encontrado:
        print("Centro no encontrado.")

resolver_turismo()
