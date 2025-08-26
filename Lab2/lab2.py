class Libro:
    def __init__(self, titulo, autor, anio, ejemplares):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.ejemplares = ejemplares
        self.disponible = ejemplares > 0

    def prestar(self):
        if self.ejemplares > 0:
            self.ejemplares -= 1
            self.disponible = self.ejemplares > 0
            print(f" Se ha prestado '{self.titulo}'. Ejemplares restantes: {self.ejemplares}")
        else:
            print(f" El libro '{self.titulo}' no está disponible.")

    def devolver(self):
        self.ejemplares += 1
        self.disponible = True
        print(f"Se ha devuelto '{self.titulo}'. Ejemplares disponibles: {self.ejemplares}")

    def __str__(self):
        estado = "Disponible" if self.disponible else "No disponible"
        return f"{self.titulo} - {self.autor} ({self.anio}) | Ejemplares: {self.ejemplares} | {estado}"


class Libreria:
    def __init__(self):
        self.catalogo = []

    def registrar_libro(self, titulo, autor, anio, ejemplares):
        nuevo_libro = Libro(titulo, autor, anio, ejemplares)
        self.catalogo.append(nuevo_libro)
        print(f" Se ha registrado el libro: {titulo}")

    def mostrar_catalogo(self):
        if not self.catalogo:
            print(" No hay libros registrados.")
        else:
            print("\n Catálogo de libros:")
            for libro in self.catalogo:
                print(libro)

    def buscar_libro(self, titulo):
        for libro in self.catalogo:
            if libro.titulo.lower() == titulo.lower():
                return libro
        return None



def menu():
    libreria = Libreria()

    while True:
        print("\nII===== Bienveido a Libreria Armando=====II")
        print("1. Registrar libros")
        print("2. Catalogo de libros")
        print("3. Prestar libro")
        print("4. Devolver libro")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            titulo = input("Título del libro: ")
            autor = input("Autor: ")
            anio = input("Año de publicado: ")
            ejemplares = int(input("Cantidad de ejemplares: "))
            libreria.registrar_libro(titulo, autor, anio, ejemplares)

        elif opcion == "2":
            libreria.mostrar_catalogo()

        elif opcion == "3":
            titulo = input("Ingrese el título del libro a prestar: ")
            libro = libreria.buscar_libro(titulo)
            if libro:
                libro.prestar()
            else:
                print(" Libro no encontrado.")

        elif opcion == "4":
            titulo = input("Ingrese el título del libro a devolver: ")
            libro = libreria.buscar_libro(titulo)
            if libro:
                libro.devolver()
            else:
                print(" Libro no encontrado.")

        elif opcion == "5":
            print(" Saliendo del sistema...")
            break

        else:
            print(" Opción no válida, intente de nuevo.")



menu()
