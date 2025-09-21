from gestion import GestionConsumo

def main():
    print("📊 Sistema de Control de Consumo Eléctrico\n")

    costo_kwh = float(input("Ingrese el costo por kWh en dólares: "))
    gestion = GestionConsumo(costo_kwh)

    while True:
        nombre = input("\nIngrese el nombre del aparato: ")
        potencia = float(input("Ingrese la potencia en Watts: "))
        horas = float(input("Ingrese las horas de uso al mes: "))

        gestion.agregar_aparato(nombre, potencia, horas)

        continuar = input("¿Desea agregar otro aparato? (s/n): ").lower()
        if continuar != 's':
            break

    gestion.mostrar_aparatos()
    gestion.resumen()

if __name__ == "__main__":
    main()
