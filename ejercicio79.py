
while True:
    class Autor:
        def __init__(self, apellido):
            self.apellido = apellido
            self.libros = []

        def agregar_libro(self, codigo, genero, paginas):
            self.libros.append({'codigo': codigo, 'genero': genero, 'paginas': paginas})

        def total_paginas(self):
            return sum(libro['paginas'] for libro in self.libros)

        def libro_mayor_paginas(self):
            if not self.libros:
                return None
            return max(self.libros, key=lambda libro: libro['paginas'])

    autores = []
    total_libros = 0
    ciencia_ficcion_count = 0
    romance_count = 0

    while True:
        apellido = input("Ingrese el apellido del autor (o 'salir' para terminar): ")
        if apellido.lower() == 'salir':
            break

        autor = Autor(apellido)

        while True:
            codigo = input("Ingrese el código del libro (o 'fin' para terminar): ")
            if codigo.lower() == 'fin':
                break
            genero = input("Ingrese el género del libro: ")
            paginas = int(input("Ingrese el número de páginas del libro: "))
            autor.agregar_libro(codigo, genero, paginas)

            total_libros += 1
            if genero.lower() == 'ciencia ficción':
                ciencia_ficcion_count += 1
            elif genero.lower() == 'romance':
                romance_count += 1

        autores.append(autor)

    
    for autor in autores:
        print(f"Autor: {autor.apellido}")
        print(f"Total de páginas escritas: {autor.total_paginas()}")
        mayor_libro = autor.libro_mayor_paginas()
        if mayor_libro:
            print(f"Código del libro con mayor número de páginas: {mayor_libro['codigo']}, Páginas: {mayor_libro['paginas']}")

    if total_libros > 0:
        porcentaje_ciencia_ficcion = (ciencia_ficcion_count / total_libros) * 100
        print(f"Porcentaje de libros de ciencia ficción respecto al total de libros: {porcentaje_ciencia_ficcion:.2f}%")
    print(f"Cantidad de libros de ciencia ficción y romance en existencia: {ciencia_ficcion_count + romance_count}")


    if autores:
        autor_mayor_libros = max(autores, key=lambda autor: len(autor.libros))
        print(f"Autor con mayor cantidad de libros escritos: {autor_mayor_libros.apellido}, Cantidad de libros: {len(autor_mayor_libros.libros)}")
    else:
        print("No se ingresaron autores.")