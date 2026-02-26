
tres_correctas = 0
solo_1_y_2 = 0
solo_1_y_3 = 0
solo_2_y_3 = 0
al_menos_1 = 0
al_menos_2 = 0
al_menos_3 = 0
ninguna_correcta = 0


total_personas = 100

for i in range(total_personas):
    print("\n--- Persona número:", i + 1, "---")
    
    p1 = int(input("Pregunta 1 (1:Correcta, 0:Incorrecta): "))
    p2 = int(input("Pregunta 2 (1:Correcta, 0:Incorrecta): "))
    p3 = int(input("Pregunta 3 (1:Correcta, 0:Incorrecta): "))

    
    if p1 == 1 and p2 == 1 and p3 == 1:
        tres_correctas += 1

    
    if p1 == 1 and p2 == 1 and p3 == 0:
        solo_1_y_2 += 1

    
    if p1 == 1 and p2 == 0 and p3 == 1:
        solo_1_y_3 += 1

    
    if p1 == 0 and p2 == 1 and p3 == 1:
        solo_2_y_3 += 1

    
    if p1 == 1:
        al_menos_1 += 1
    if p2 == 1:
        al_menos_2 += 1
    if p3 == 1:
        al_menos_3 += 1


    if p1 == 0 and p2 == 0 and p3 == 0:
        ninguna_correcta += 1


print("a. Correctas las tres preguntas:", tres_correctas)
print("b. Solamente primera y segunda:", solo_1_y_2)
print("c. Solamente primera y tercera:", solo_1_y_3)
print("d. Solamente segunda y tercera:", solo_2_y_3)
print("e. Primera por lo menos:", al_menos_1)
print("f. Segunda por lo menos:", al_menos_2)
print("g. Tercera por lo menos:", al_menos_3)
print("h. Ninguna pregunta correcta:", ninguna_correcta)
