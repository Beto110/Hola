#len()
#Descripción: Devuelve la longitud (cantidad de elementos) de un objeto iterable.
#Caso de uso: Contar la cantidad de caracteres en una contraseña ingresada.

contraseña = "MiClaveSegura123"
if len(contraseña) < 8:
    print("Contraseña demasiado corta")
else:
    print("Contraseña aceptada")


#type()
#Descripción: Devuelve el tipo de un objeto.
#Caso de uso: Validar si el dato ingresado es del tipo esperado en un formulario.

edad = 25
if type(edad) == int:
    print("Edad válida")
else:
    print("Error: la edad debe ser un número")


#sum()
#Descripción: Retorna la suma de todos los elementos de un iterable.
#Caso de uso: Calcular el total de una factura de productos.

precios = [10.5, 20.75, 5.99]
total = sum(precios)
print(f"Total a pagar: ${total}")


#max()
#Descripción: Retorna el valor máximo de un iterable.
#Caso de uso: Determinar la temperatura más alta del día.

temperaturas = [28, 32, 29, 35, 30]
print("Temperatura máxima:", max(temperaturas))


#min()
#Descripción: Retorna el valor mínimo de un iterable.
#Caso de uso: Obtener el precio más barato entre varias opciones.

precios = [150, 125, 200, 175]
print("Precio más barato:", min(precios))


#sorted()
#Descripción: Devuelve una lista ordenada a partir de un iterable.
#Caso de uso: Ordenar alfabéticamente una lista de nombres de estudiantes.

nombres = ["Carlos", "Ana", "Beatriz", "David"]
nombres_ordenados = sorted(nombres)
print(nombres_ordenados)


#round()
#Descripción: Redondea un número al entero más cercano o a cierta cantidad de decimales.
#Caso de uso: Mostrar precios con solo dos decimales.

precio = 19.987
precio_redondeado = round(precio, 2)
print(f"Precio: ${precio_redondeado}")


#abs()
#Descripción: Devuelve el valor absoluto de un número.
#Caso de uso: Calcular la diferencia sin importar el orden entre dos fechas.

diferencia = abs(2025 - 2015)
print("Años de diferencia:", diferencia)


#enumerate()
#Descripción: Añade un contador a un iterable y lo devuelve en forma de tuplas.
#Caso de uso: Numerar los elementos de una lista en un menú.

menu = ["Pizza", "Hamburguesa", "Ensalada"]
for i, plato in enumerate(menu, start=1):
    print(f"{i}. {plato}")


#zip()
#Descripción: Une dos o más iterables elemento a elemento.
#Caso de uso: Emparejar nombres de productos con sus precios.

productos = ["Camisa", "Pantalón", "Zapatos"]
precios = [20, 30, 50]
for producto, precio in zip(productos, precios):
    print(f"{producto}: ${precio}")


#all()
#Descripción: Retorna True si todos los elementos de un iterable son verdaderos.
#Caso de uso: Verificar si todos los campos de un formulario fueron llenados.

campos = ["Nombre", "Apellido", "Correo"]
datos = ["Juan", "Pérez", "juan@mail.com"]
print("Formulario completo:", all(datos))


#any()
#Descripción: Retorna True si al menos un elemento de un iterable es verdadero.
#Caso de uso: Verificar si hay alguna alerta activa en un sistema.

alertas = [False, False, True]
if any(alertas):
    print("¡Alerta activa!")


#range
#Descripción: Genera una secuencia de números enteros.
#Caso de uso: Crear un listado del 1 al 10 para un cuestionario.

for numero in range(1, 11):
    print(f"Pregunta {numero}")


#reversed()
#Descripción: Devuelve un iterador que recorre una secuencia en orden inverso.
#Caso de uso: Mostrar un historial de acciones del usuario desde la más reciente.

acciones = ["login", "ver perfil", "editar", "cerrar sesión"]
for accion in reversed(acciones):
    print(accion)


#bool()
#Descripción: Convierte un valor a tipo booleano.
#Caso de uso: Verificar si una cadena contiene texto

nombre = "Carlos"
if bool(nombre):
    print("Nombre ingresado")


#int()
#Descripción: Convierte un valor a entero.
#Caso de uso: Convertir la edad ingresada como texto a número.

edad_texto = "18"
edad = int(edad_texto)
print(f"Tendrás {edad + 1} años el próximo año")


#float()
#Descripción: Convierte un valor a número decimal.
#Caso de uso: Ingresar calificaciones con decimales.

nota = float("8.75")
print("Nota registrada:", nota)


#str()
#Descripción: Convierte un valor a cadena de texto.
#Caso de uso: Mostrar resultados numéricos como texto en mensajes.

puntos = 100
mensaje = "Has ganado " + str(puntos) + " puntos."
print(mensaje)


#set()
#Descripción: Crea un conjunto (sin elementos duplicados).
#Caso de uso: Eliminar duplicados de una lista de correos.

correos = ["a@mail.com", "b@mail.com", "a@mail.com"]
correos_unicos = set(correos)
print(correos_unicos)


#list()
#Descripción: Convierte un iterable a una lista.
#Caso de uso: Convertir los caracteres de una palabra a lista para analizarla.

palabra = "robot"
letras = list(palabra)
print(letras)