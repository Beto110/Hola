class Socio:
    def __init__(self, nombre, edad, telefono, membresia):
        self.nombre = nombre
        self.edad = edad
        self.telefono = telefono
        self.membresia = membresia
        self.beneficios = self.asignar_beneficios()

    def asignar_beneficios(self):
        beneficios_por_membresia = {
            "Básica": ["Acceso al gimnasio en el horario establecido"],
            "Premium": ["Acceso al gimnasio en horario normal", "Clases grupales", "Uso de sauna"],
            "VIP": ["Acceso 24/7 al gym", "Clases personalizadas", "Uso de sauna", "Nutricionista", "Descuentos en productos", "Acceso a eventos exclusivos", "Asesoría personalizada", "Zona VIP"]
        }
        return beneficios_por_membresia.get(self.membresia, ["Sin beneficios asignados"])

    def __str__(self):
        return (f" {self.nombre} | Edad: {self.edad} | Tel: {self.telefono} | "
                f"Membresía: {self.membresia}\n   Beneficios: {', '.join(self.beneficios)}")


class Gimnasio:
    def __init__(self):
        self.socios = []

    def registrar_socio(self, nombre, edad, telefono, membresia):
        nuevo_socio = Socio(nombre, edad, telefono, membresia)
        self.socios.append(nuevo_socio)
        print(f" Socio {nombre} registrado con membresía {membresia}.")

    def mostrar_socios(self):
        if not self.socios:
            print(" No hay socios registrados.")
        else:
            print("\n Lista de socios del gimnasio:")
            for socio in self.socios:
                print(socio)


# ---- Menú interactivo ----
def menu():
    gimnasio = Gimnasio()

    while True:
        print("\nII===== 180 FITNESS GYM =====II")
        print("1. Registrar socio")
        print("2. Mostrar socios")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            edad = input("Edad: ")
            telefono = input("Teléfono: ")

            print("\nTipos de membresía disponibles:")
            print("1. Básica")
            print("2. Premium")
            print("3. VIP")

            tipo = input("Seleccione el tipo de membresía: ")
            if tipo == "1":
                membresia = "Básica"
            elif tipo == "2":
                membresia = "Premium"
            elif tipo == "3":
                membresia = "VIP"
            else:
                print(" Tipo no válido, se asignará 'Básica'")
                membresia = "Básica"

            gimnasio.registrar_socio(nombre, edad, telefono, membresia)

        elif opcion == "2":
            gimnasio.mostrar_socios()

        elif opcion == "3":
            print(" Saliendo del sistema...")
            break

        else:
            print(" Opción no válida, intente de nuevo.")



menu()
