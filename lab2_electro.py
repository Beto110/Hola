class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def mostrar_info(self):
        return f"{self.nombre} | Precio: ${self.precio}"


class Televisor(Producto):
    def __init__(self, nombre, precio, pulgadas):
        super().__init__(nombre, precio)
        self.pulgadas = pulgadas

    def mostrar_info(self):
        return f" Televisor: {self.nombre} | {self.pulgadas}\" | Precio: ${self.precio}"


class Smartphone(Producto):
    def __init__(self, nombre, precio, almacenamiento):
        super().__init__(nombre, precio)
        self.almacenamiento = almacenamiento

    def mostrar_info(self):
        return f" Smartphone: {self.nombre} | {self.almacenamiento} GB | Precio: ${self.precio}"


class Tienda:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)
        print(f" Producto '{producto.nombre}' agregado a la tienda.")

    def mostrar_productos(self):
        if not self.productos:
            print(" No hay productos en la tienda.")
        else:
            print("\n Catálogo de productos:")
            for prod in self.productos:
                print(prod.mostrar_info())


# ---- Con este Menú se interactua ----
def menu():
    tienda = Tienda()

    while True:
        print("\nII===== MENÚ TIENDA DE ELECTRÓNICOS Armando =====II")
        print("1. Agregar Televisor")
        print("2. Agregar Telefono")
        print("3. Productos disponibles")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del televisor: ")
            precio = float(input("Precio: $"))
            pulgadas = int(input("Pulgadas: "))
            tv = Televisor(nombre, precio, pulgadas)
            tienda.agregar_producto(tv)

        elif opcion == "2":
            nombre = input("Nombre del smartphone: ")
            precio = float(input("Precio: $"))
            almacenamiento = int(input("Capacidad de almacenamiento (GB): "))
            phone = Smartphone(nombre, precio, almacenamiento)
            tienda.agregar_producto(phone)

        elif opcion == "3":
            tienda.mostrar_productos()

        elif opcion == "4":
            print(" Saliendo del sistema...")
            break

        else:
            print(" Opción no válida, intente de nuevo.")


# Ejecuta el menú
menu()


#¿Por qué es útil separar la información común de la específica de cada tipo de producto?
# Separar la información común puede permite reutilizar códigos y facilita la expansion del sistema.

#¿Si la tienda agrega nuevos tipos de productos, ¿cómo modificaría su diseño sin rehacer todo el sistema?
# Podría crear nuevas clases que hereden de la clase Producto, manteniendo la estructura y funcionalidad existente.
