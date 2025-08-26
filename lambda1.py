def suma(n1, n2):
    return n1 + n2
print(suma(4, 5))

suma = lambda n1, n2: n1 + n2
print(suma(4, 5))

nombre = lambda nom, ape:f"Mi nombre completo es {nom} {ape}"
print(nombre("Juan", "Pérez"))

def potencia(num):
    return lambda x:x ** num

numero = potencia(5)
print(numero(20))

